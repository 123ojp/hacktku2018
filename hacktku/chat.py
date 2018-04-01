# -*- coding: utf-8 -*-
import json
import read_db

from gevent import monkey
monkey.patch_all()

from flask import Flask, app, render_template
from werkzeug.debug import DebuggedApplication

from geventwebsocket import WebSocketServer, WebSocketApplication, Resource

flask_app = Flask(__name__)
flask_app.debug = True



class ChatApplication(WebSocketApplication):
    def on_open(self):
        pass
        # print "Some client connected!"

    def on_message(self, message):
        if message is None:
            return
        #for client in self.ws.handler.server.clients.values():
        #    if client.address == :
        #        client.ws.send()
        #print dir(self.ws.handler.server.clients.values)
        message = json.loads(message)
        #print dir(self.ws.handler.active_client)

        # if message['msg_type'] == 'message':
        #     self.broadcast(message)
        # elif message['msg_type'] == 'update_clients':
        #     self.send_client_list(message)
        if message['msg_type'] == 'answer':
            self.check_answer(message)
        elif message['msg_type'] == 'waiting_fight':
            self.waiting_fight(message)
        elif message['msg_type'] == 'over_question':
            self.over_question(message)
        elif message['msg_type'] == 'hello':
            self.make_hello(message)
        elif message['msg_type'] == 'start_ques':
            self.start_ques(message)


    # def send_client_list(self, message):
    #     current_client = self.ws.handler.active_client
    #     current_client.nickname = message['nickname']
    #
    #     self.ws.send(json.dumps({
    #         'msg_type': 'update_clients',
    #         'clients': [
    #             getattr(client, 'nickname', 'anonymous')
    #             for client in self.ws.handler.server.clients.values()
    #         ]
    #     }))
    #
    # def broadcast(self, message):
    #     for client in self.ws.handler.server.clients.values():
    #         client.ws.send(json.dumps({
    #             'msg_type': 'message',
    #             'nickname': message['nickname'],
    #             'message': message['message']
    #         }))

    def on_close(self, reason):
        print ("Connection closed! ")
        nickname=self.ws.handler.active_client.nickname
        #砍掉DB資料 (question_readquestion)
        read_db.Rm_data(nickname)

    def waiting_fight(self,message):
        nickname = message['nickname']
        #place = message['']# 位子
        Waspair=read_db.Had_pair(nickname)#False #問db有沒有
        if Waspair:
            #DB getquestion
            send_question ,teamate = read_db.get_question(nickname)
            self.ws.send(json.dumps({
                'msg_type': 'waiting_respon',
                'people':1,
                'teamate':teamate
            }))
            self.ws.handler.active_client.teamate = teamate

        else:
            self.ws.send(json.dumps({
                'msg_type': 'waiting_respon',
                'people':0
            }))
    def check_answer(self,message):
        nickname = message['nickname']
        answer = message['answer']
        correct = read_db.check_correct(nickname,answer)#False #問db對不對
        score = read_db.get_score(nickname)#跟db拿成績
        teamate=self.ws.handler.active_client.teamate
        score_team=read_db.get_score(teamate)
        if (correct):
            score +=100
            score_team+=100
            read_db.add_score(nickname,score) #把db score 改掉 =score
            read_db.add_score(teamate,score_team)
            self.ws.send(json.dumps({
                'msg_type': 'answer_respon',
                'correct':1,
                'score':score
            }))
            for client in self.ws.handler.server.clients.values():
                if client.ws.handler.active_client.nickname==teamate:
                    client.ws.send(json.dumps({
                         'msg_type': 'answer_respon',
                         'correct':1,
                         'score':score_team
                     }))

        else:
            self.ws.send(json.dumps({
                'msg_type': 'answer_respon',
                'correct':0,
                'score':score
            }))
            for client in self.ws.handler.server.clients.values():
                if client.ws.handler.active_client.nickname==teamate:
                     client.ws.send(json.dumps({
                        'msg_type': 'answer_respon',
                        'correct':0,
                        'score':score_team
                     }))
        read_db.same_new_fight(nickname)
        read_db.same_new_fight(teamate)

    def over_question(self,message):
        nickname = message['nickname']
        #db 寫入重新配對
        read_db.new_fight(nickname)
    def make_hello(self,message):
        nickname = message['nickname']
        self.ws.handler.active_client.nickname=nickname
        #建立新資料到db (question_readquestion)
        read_db.add_data(nickname)
    def start_ques(self,message):
        nickname = message['nickname']
        send_question ,teamate = read_db.get_question(nickname)
        self.ws.send(json.dumps({
            'msg_type': 'question',
            'question': send_question,
        }))





@flask_app.route('/')
def index():
    return render_template('index.html')
#thread.start_new_thread(makequs.lookingDB_thread(), ("Thread-1", 4, ) )

WebSocketServer(
    ('127.0.0.1', 8080),

    Resource([
        ('^/chat', ChatApplication),
        ('^/.*', DebuggedApplication(flask_app))
    ]),

    debug=False
).serve_forever()
