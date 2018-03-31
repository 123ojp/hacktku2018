# -*- coding: utf-8 -*-
import random, itertools


def qus_sex(data1, data2):
    qus = '題目:請從以下四個選項，回答兩位的"性別"組合為何?'
    ans = '["男男","男女","女女","以上皆非"]'

    if data1 == "男" and data2 == "男":
        ans_num = 0
    elif data1 == "女" and data2 == "男" or data1 == "男" and data2 == "女":
        ans_num = 1
    elif data1 == "女" and data2 == "女":
        ans_num = 2
    else:
        ans_num = 3
    return qus, ans, str(ans_num)


def qus_school(data1, data2):
    qus = '題目:請從以下四個選項，回答兩位之中的最高學歷為何?'
    if data1 == "科大" or data1 == "大學":
        data1 = '大學/科大'
    if data2 == "科大" or data2 == "大學":
        data2 = '大學/科大'
    if data1 == "高中" or data1 == "高職":
        data1 = '高中/高職'
    if data2 == "高中" or data2 == "高職":
        data2 = '高中/高職'
    ans_data = ['國小', '國中', '高中/高職', '大學/科大', '碩士生', '博士生']
    count = 0
    for i in range(5, -1, -1):
        if ans_data[i] == data1 or ans_data[i] == data2:
            break
        count = i
    ans = []
    ans.append(ans_data.pop(count - 1))
    ans.append(ans_data.pop(random.randrange(len(ans_data))))
    ans.append(ans_data.pop(random.randrange(len(ans_data))))
    ans.append(ans_data.pop(random.randrange(len(ans_data))))
    ans_num = 0
    return qus, str(ans), str(ans_num)


def qus_num(data1, data2):
    qus = '題目:請從以下四個選項，回答兩位"最喜歡的數字"相加除以2為何(無條件捨去)?'
    ans_data = list(range(0, 11))
    ans = []
    try:
        ans.append(ans_data.pop(int((int(data1) + int(data2)) / 2)))
    except:
        ans.append(int((int(data1) + int(data2)) / 2))
    ans.append(ans_data.pop(random.randrange(len(ans_data))))
    ans.append(ans_data.pop(random.randrange(len(ans_data))))
    ans.append(ans_data.pop(random.randrange(len(ans_data))))
    ans_num = 0
    return qus, str(ans), str(ans_num)


def qus_star(data1, data2):
    qus = '題目:請從下列三個選項，選出非兩者的星座為何?'
    ans = []
    ans_data = ['水瓶座', '雙魚座', '牡羊座', '金牛座', '雙子座', '巨蟹座', '獅子座', '處女座', '天秤座', '天蠍座', '射手座', '摩羯座']
    if data1 in ans_data:
        ans_data.remove(data1)
    if data2 in ans_data:
        ans_data.remove(data2)
    ans.append(data1)
    ans.append(data2)
    ans.append(ans_data.pop(random.randrange(len(ans_data))))
    ans_num = 2
    ans.append("不要選我")
    return qus, str(ans), str(ans_num)


def qus_name(data1, data2, data3, data4):
    qus = '題目:請從以下四個選項，選出兩位的其一的"姓"與其一的"名字"加起來為何?'
    ans = [data1 + data2, data3 + data4, data1 + data3, data3 + data2]
    ans_num = 4
    return qus, ans, str(ans_num)


def qus_yearadd(data1, data2):
    a = int(data1.split('-')[0])
    b = int(data2.split('-')[0])
    qus = '題目:請從以下四個選項，回答兩位的"出生年"相加為何數'
    ans = [a + b + 1, a + b, a + b + 3, a + b + b]
    ans_num = 2
    return qus, ans, str(ans_num)


def qus_yearcompare(data1, data2):
    a = int(data1.split('-')[0])
    b = int(data2.split('-')[0])
    qus = '題目:請從以下四個選項，回答兩位的年紀相差多少?(出生年-出生年)'
    if a > b:
        tmp = a - b
    else:
        tmp = b - a
    ans = [tmp + 1, tmp + 3, tmp, tmp - 1]
    ans_num = 3
    return qus, ans, str(ans_num)


def qus_monthadd(data1, data2):
    a = int(data1.split('-')[1])
    b = int(data2.split('-')[1])
    qus = '題目:請從以下四個選項，回答兩位的"出生月"相加再除以2為何數(無條件捨去)?'
    ans = [int((a + b + 1) / 2), int((a + b + 3) / 2), int((a + b + b) / 2), int((a + b) / 2)]
    ans_num = 4
    return qus, ans, str(ans_num)


def qus_home(data1, data2):
    home = ['臺北市', '新北市', '宜蘭縣', '桃園市', '新竹縣', '新竹市', '苗栗縣', '臺中市', '彰化縣', '南投縣', '基隆市', '雲林縣', '嘉義市', '嘉義縣', '臺南市',
            '高雄市', '屏東縣', '臺東縣', '花蓮縣', '澎湖縣', '金門縣', '連江縣']
    qus = '題目:請從以下四個選項，回答兩位的"出生地"為何?'
    if data1 in home:
        home.remove(data1)
    if data2 in home:
        home.remove(data2)
    ans = ''
    ans_data = list(itertools.permutations(home, 2))
    ans = list(random.sample(ans_data, 3))
    for i, j in enumerate(ans):
        ans[i] = "/".join(j)
    ans.append(data1 + '/' + data2)
    ans_num = 4
    return qus, ans, str(ans_num)


def qus_star(data1, data2):
    star = ['水瓶座', '雙魚座', '牡羊座', '金牛座', '雙子座', '巨蟹座', '獅子座', '處女座', '天秤座', '天蠍座', '射手座', '摩羯座']
    qus = '題目:請從以下四個選項，回答兩位的"星座"為何?'
    if data1 in star:
        star.remove(data1)
    if data2 in star:
        star.remove(data2)
    ans = ''
    ans_data = list(itertools.permutations(star, 2))
    ans = list(random.sample(ans_data, 3))
    for i, j in enumerate(ans):
        ans[i] = "/".join(j)
    ans.append(data1 + '/' + data2)
    ans_num = 4
    return qus, ans, str(ans_num)


def qus_edu(data1, data2):
    edu = ['國小', '國中', '高中', '高職', '大學', '科大', '碩士生', '博士生']
    qus = '題目:請從以下四個選項，回答兩位之中的"學歷"組合為何'
    if data1 in edu:
        edu.remove(data1)
    if data2 in edu:
        edu.remove(data2)
    ans = ''
    ans_data = list(itertools.permutations(edu, 2))
    ans = list(random.sample(ans_data, 3))
    for i, j in enumerate(ans):
        ans[i] = "/".join(j)
    ans.append(data1 + '/' + data2)
    ans_num = 4
    return qus, ans, str(ans_num)


def qus_fruit(data1, data2):
    fruit = ['蘋果', '西瓜', '桃子', '芭樂', '木瓜', '哈密瓜', '蕃茄', '櫻桃', '草莓', '鳳梨', '葡萄', '香蕉', '楊桃', '荔枝', '百香果', '奇異果', '芒果',
             '柳橙', '蓮霧']
    qus = '題目:請從以下四個選項，回答兩位的"水果"組合為何'
    if data1 in fruit:
        fruit.remove(data1)
    if data2 in fruit:
        fruit.remove(data2)
    ans = ''
    ans_data = list(itertools.permutations(fruit, 2))
    ans = list(random.sample(ans_data, 3))
    for i, j in enumerate(ans):
        ans[i] = "/".join(j)
    ans.append(data1 + '/' + data2)
    ans_num = 4
    return qus, ans, str(ans_num)


def qus_color(data1, data2):
    color = ['紅色', '橙色', '黃色', '綠色', '藍色', '紫色', '黑色', '白色']
    qus = '題目:請從以下四個選項，回答兩位的"水果"組合為何'
    if data1 in color:
        color.remove(data1)
    if data2 in color:
        color.remove(data2)
    ans = ''
    ans_data = list(itertools.permutations(color, 2))
    ans = list(random.sample(ans_data, 3))
    for i, j in enumerate(ans):
        ans[i] = "/".join(j)
    ans.append(data1 + '/' + data2)
    ans_num = 4
    return qus, ans, str(ans_num)
