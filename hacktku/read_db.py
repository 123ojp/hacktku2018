import sqlite3,os,requests,json
db = sqlite3.connect('./db.sqlite3', check_same_thread=False)

c = db.cursor()

def Had_pair(nickname):
    list = db.execute("SELECT status  from question_readquestion WHERE user_id = '"+str(nickname)+"';")
    list3=[]
    for data in list:
        list3.append(data[0])
    try :
        if list3[0]==True:
            return True
    except:
        return False
    else:
        return False

def Rm_data(nickname):
    c.execute("DELETE from question_readquestion where user_id='"+str(nickname)+"';")
    db.commit()

def add_data(nickname):
    max_read = db.execute("SELECT COALESCE(MAX(id)+1, 0) FROM question_readquestion")
    for i in max_read:
        max = str(i[0])
    c.execute("INSERT INTO  question_readquestion (id,status,answer,user_id,question,teamate) \
                        VALUES ('"+max+"','0','0','"+str(nickname)+"','0','0')");
    db.commit()
def get_question(nickname):
    list = db.execute("SELECT question  from question_readquestion WHERE user_id = '"+str(nickname)+"';")
    list3=[]
    for data in list:
        #print data
        list3.append(data[0])
    list1 = db.execute("SELECT teamate  from question_readquestion WHERE user_id = '"+str(nickname)+"';")
    list2 =[]
    for data in list1:
        #print data
        list2.append(data[0])
    try :
        return str(list3[0]),str(list2[0])
    except:
        return "Server Error","Server Error"
def check_correct(nickname,answer):
    list = db.execute("SELECT answer from question_readquestion WHERE user_id = '"+str(nickname)+"';")
    list3=[]
    for data in list:
        #print data
        list3.append(data[0])
    try:
        if int(list3[0])==int(answer):
            return True
        else :
            return False
    except:
        return False
def new_fight(nickname):
    c.execute("UPDATE   question_readquestion SET status='0' \
                        WHERE user_id = '"+str(nickname)+"';")
    db.commit()
def same_new_fight(nickname):
    c.execute("UPDATE   question_readquestion SET status='3' \
                        WHERE user_id = '"+str(nickname)+"';")
    db.commit()

def get_score(nickname):
    respon = requests.get("http://127.0.0.1:8000/api/userprofile/" + str(nickname) + "/?format=json")
    jsondata = json.loads(respon.text)
    score = str(jsondata['score'])
    return int(score)


def add_score(nickname, score):
    payload = {
        "id": nickname,
        "score": score
    }
    r = requests.put('http://127.0.0.1:8000/api/userprofile/' + str(nickname) + '/', json=payload)


#print new_fight(2)
