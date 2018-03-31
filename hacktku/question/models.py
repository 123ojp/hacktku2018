from django.contrib.auth.models import User, AbstractUser
from django.db import models

import uuid

# Create your models here.


class UserProfile(AbstractUser):
    NUM_CHOICES = [(str(i),(str(i))) for i in range(1,11)]
    birthday = models.DateField(null=True, blank=False,verbose_name=u'生日')
    phone = models.CharField(null=False, blank=False,verbose_name=u'手機號碼',max_length=10)
    address = models.CharField(null=False, blank=False,max_length=20, choices=(('臺北市','臺北市'), ('新北市', '新北市'), ('宜蘭縣', '宜蘭縣'), ('桃園市', '桃園市'), ('新竹縣', '新竹縣'), ('新竹市', '新竹市'), ('苗栗縣', '苗栗縣'), ('臺中市', '臺中市'), ('彰化縣', '彰化縣'), ('南投縣', '南投縣'), ('基隆市', '基隆市'), ('嘉義縣', '嘉義縣'), ('臺南市', '臺南市'), ('高雄市', '高雄市'), ('屏東縣', '屏東縣'), ('臺東縣', '臺東縣'), ('花蓮縣', '花蓮縣'), ('澎湖縣', '澎湖縣'), ('金門縣', '金門縣'), ('連江縣', '連江縣')), default='臺北市', verbose_name=u'縣市')
    coler = models.CharField(null=False, blank=False, choices=(('紅色','紅色'),('橙色','橙色'),('黃色','黃色'),('綠色','綠色'),('藍色','藍色'),('紫色 ','紫色'),('黑色','黑色'),('白色','白色')),default='紅色',verbose_name=u'喜歡顏色',max_length=10)
    fruit = models.CharField(null=False, blank=False,max_length=20, choices=(('蘋果','蘋果'),('西瓜','西瓜'),('桃子','桃子'),('芭樂','芭樂'),('木瓜','木瓜'),('哈密瓜','哈密瓜'),('蕃茄','蕃茄'),('櫻桃','櫻桃'),('草莓','草莓'),('鳳梨','鳳梨'),('葡萄','葡萄'),('香蕉','香蕉'),('楊桃','楊桃'),('荔枝','荔枝'),('百香果','百香果'),('奇異果','奇異果'),('芒果','芒果'),('柳橙','柳橙'),('蓮霧','蓮霧')), default='草莓', verbose_name=u'喜愛水果')
    num = models.CharField(null=False, blank=False,max_length=6,choices=NUM_CHOICES,verbose_name=u'喜愛數字')
    constellation = models.CharField(null=False, blank=False,max_length=20, choices=(('水瓶座','水瓶座'), ('雙魚座', '雙魚座'), ('牡羊座', '牡羊座'), ('金牛座', '金牛座'), ('雙子座', '雙子座'), ('巨蟹座', '巨蟹座'), ('獅子座', '獅子座'), ('處女座', '處女座'), ('天秤座', '天秤座'), ('天蠍座', '天蠍座'), ('射手座', '射手座'), ('摩羯座', '摩羯座')), default='水瓶座', verbose_name=u'所屬星座'                                                                                                                                                                                                                                                                                                         u'')
    gender = models.CharField(null=False, blank=False,max_length=6, choices=(('男','男'), ('女', '女')), default='女', verbose_name=u'性別')
    blood = models.CharField(null=False, blank=False,max_length=6, choices=(('A','A'), ('B','B'),('AB','AB'),('O','O')), default='A', verbose_name=u'血型')
    education = models.CharField(null=False, blank=False,max_length=20, choices=(('國小','國小'),('國中','國中'),('高中','高中'),('高職','高職'),('大學','大學'),('科大','科大'),('碩士生','碩士生'),('博士生','博士生')), default='大學', verbose_name=u'學歷')
    stamp_created = models.DateTimeField(auto_now_add=True, verbose_name='問題新增時間')
    stamp_updated = models.DateTimeField(auto_now=True, verbose_name='問題更新時間')
    score = models.IntegerField(default=0, verbose_name='分數')

# class Answer(models.Model):
#     user = models.ForeignKey(UserProfile, on_delete=models.CASCADE,verbose_name=u'所屬者',null=True)

class Question(models.Model):
    question = models.TextField( verbose_name=u'題目')

class Readquestion(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE,verbose_name=u'所屬者',null=True)
    status = models.IntegerField(default=0,verbose_name=u'目前狀態')
    question = models.TextField(null=True, blank=True,default='',verbose_name=u'題目/答案')
    answer = models.TextField(null=True, blank=True,default='',verbose_name=u'真正的答案')
    teamate = models.CharField(null=False, blank=False,default='',verbose_name=u'對應對手',max_length=10)
