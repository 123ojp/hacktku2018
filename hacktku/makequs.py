# -*- coding: utf-8 -*-
import sqlite3,os,time,random,requests,json,urllib.parse

import qus_list
db = sqlite3.connect('./db.sqlite3', check_same_thread=False)
c = db.cursor()
class switch(object):
    def __init__(self, value):
        self.value = value
        self.fall = False

    def __iter__(self):
        """Return the match method once, then stop"""
        yield self.match
        raise StopIteration

    def match(self, *args):
        """Indicate whether or not to enter a case suite"""
        if self.fall or not args:
            return True
        elif self.value in args: # changed for v1.5, see below
            self.fall = True
            return True
        else:
            return False

def find_unpair():
    list = db.execute("SELECT user_id  from question_readquestion WHERE status = '0';")
    list3=[]
    for data in list:
        list3.append(data[0])
    if int(len(list3)) >= 2:
        question,answer,ans_num=make_qus(str(list3[0]),str(list3[1]))#出題
        #第一個仁

        print ("UPDATE   question_readquestion SET question='"+urllib.parse.quote(str(answer))+"' \
                            WHERE user_id = '"+urllib.parse.quote(str(list3[1]))+"';")
        c.execute("UPDATE   question_readquestion SET question='"+urllib.parse.quote(str(question))+"' \
                            WHERE user_id = '"+urllib.parse.quote(str(list3[0]))+"';")
        c.execute("UPDATE   question_readquestion SET status='1' \
                            WHERE user_id = '"+urllib.parse.quote(str(list3[0]))+"';")
        c.execute("UPDATE   question_readquestion SET answer='"+urllib.parse.quote(str(ans_num))+"' \
                            WHERE user_id = '"+urllib.parse.quote(str(list3[0]))+"';")
        c.execute("UPDATE   question_readquestion SET teamate='"+urllib.parse.quote(str(list3[1]))+"' \
                            WHERE user_id = '"+urllib.parse.quote(str(list3[0]))+"';")
        #第二個仁
        c.execute("UPDATE   question_readquestion SET question='"+urllib.parse.quote(str(answer))+"' \
                            WHERE user_id = '"+urllib.parse.quote(str(list3[1]))+"';")
        c.execute("UPDATE   question_readquestion SET status='1' \
                            WHERE user_id = '"+urllib.parse.quote(str(list3[1]))+"';")
        c.execute("UPDATE   question_readquestion SET answer='"+urllib.parse.quote(str(ans_num))+"' \
                            WHERE user_id = '"+urllib.parse.quote(str(list3[1]))+"';")
        c.execute("UPDATE   question_readquestion SET teamate='"+urllib.parse.quote(str(list3[0]))+"' \
                            WHERE user_id = '"+urllib.parse.quote(str(list3[1]))+"';")
        db.commit()
def make_qus(id1,id2):
    p1_json=get_info(id1)
    p2_json=get_info(id2)
    #print p1_json
    ran=random.randrange(13)

    if ran ==0:
        qus, ans, ans_num=qus_list.qus_sex(p1_json['gender'],p2_json['gender'])
    if ran ==1:
        qus, ans, ans_num=qus_list.qus_school(p1_json['education'], p2_json['education'])
    if ran ==2:
        qus, ans, ans_num=qus_list.qus_num(p1_json['num'],p2_json['num'])
    if ran ==3:
        qus, ans, ans_num=qus_list.qus_star(p1_json['constellation'],p2_json['constellation'])
    if ran ==4:
        qus, ans, ans_num=qus_list.qus_name(p1_json['first_name'],p1_json['last_name'],p2_json['first_name'],p2_json['last_name'])
    if ran ==5:
        qus, ans, ans_num=qus_list.qus_yearadd(p1_json['birthday'],p2_json['birthday'])
    if ran ==6:
        qus, ans, ans_num=qus_list.qus_yearcompare(p1_json['birthday'],p2_json['birthday'])
    if ran ==7:
        qus, ans, ans_num=qus_list.qus_monthadd(p1_json['birthday'],p2_json['birthday'])
    if ran ==8:
        qus, ans, ans_num=qus_list.qus_home(p1_json['address'],p2_json['address'])
    if ran ==9:
        qus, ans, ans_num=qus_list.qus_star1(p1_json['constellation'],p2_json['constellation'])
    if ran ==10:
        qus, ans, ans_num=qus_list.qus_edu(p1_json['education'], p2_json['education'])
    if ran ==11:
        qus, ans, ans_num=qus_list.qus_fruit(p1_json['fruit'],p2_json['fruit'])
    if ran ==12:
        qus, ans, ans_num=qus_list.qus_color(p1_json[u'coler'],p2_json[u'coler'])

    print (qus)
    return qus, ans, ans_num

def find_paired():
    list = db.execute("SELECT user_id  from question_readquestion WHERE status = '3';")
    list3=[]
    for data in list:
        list3.append(data[0])
    if int(len(list3)) >= 2:
        question,answer,ans_num=make_qus(str(list3[0]),str(list3[1]))#出題
        #第一個仁

        print ("UPDATE   question_readquestion SET question='"+urllib.parse.quote(str(answer))+"' \
                            WHERE user_id = '"+urllib.parse.quote(str(list3[1]))+"';")
        c.execute("UPDATE   question_readquestion SET question='"+urllib.parse.quote(str(question))+"' \
                            WHERE user_id = '"+urllib.parse.quote(str(list3[0]))+"';")
        c.execute("UPDATE   question_readquestion SET status='1' \
                            WHERE user_id = '"+urllib.parse.quote(str(list3[0]))+"';")
        c.execute("UPDATE   question_readquestion SET answer='"+urllib.parse.quote(str(ans_num))+"' \
                            WHERE user_id = '"+urllib.parse.quote(str(list3[0]))+"';")
        c.execute("UPDATE   question_readquestion SET teamate='"+urllib.parse.quote(str(list3[1]))+"' \
                            WHERE user_id = '"+urllib.parse.quote(str(list3[0]))+"';")
        #第二個仁
        c.execute("UPDATE   question_readquestion SET question='"+urllib.parse.quote(str(answer))+"' \
                            WHERE user_id = '"+urllib.parse.quote(str(list3[1]))+"';")
        c.execute("UPDATE   question_readquestion SET status='1' \
                            WHERE user_id = '"+urllib.parse.quote(str(list3[1]))+"';")
        c.execute("UPDATE   question_readquestion SET answer='"+urllib.parse.quote(str(ans_num))+"' \
                            WHERE user_id = '"+urllib.parse.quote(str(list3[1]))+"';")
        c.execute("UPDATE   question_readquestion SET teamate='"+urllib.parse.quote(str(list3[0]))+"' \
                            WHERE user_id = '"+urllib.parse.quote(str(list3[1]))+"';")
        db.commit()
def lookingDB_thread():
    while 1:
        find_unpair()
        find_paired()
        time.sleep(1)

def get_info(data):
    respon = requests.get("http://127.0.0.1:8000/api/question/" + str(data) + "/?format=json")
    jsondata = json.loads(respon.text)
    return jsondata

if __name__ == '__main__':
    lookingDB_thread()
