# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-03-31 17:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0009_auto_20180331_1817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='readquestion',
            name='status',
            field=models.IntegerField(default=0, verbose_name='目前狀態'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='constellation',
            field=models.CharField(choices=[('水瓶座', '水瓶座'), ('雙魚座', '雙魚座'), ('牡羊座', '牡羊座'), ('金牛座', '金牛座'), ('雙子座', '雙子座'), ('巨蟹座', '巨蟹座'), ('獅子座', '獅子座'), ('處女座', '處女座'), ('天秤座', '天秤座'), ('天蠍座', '天蠍座'), ('射手座', '射手座'), ('摩羯座', '摩羯座')], default='水瓶座', max_length=20, verbose_name='所屬星座'),
        ),
    ]
