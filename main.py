#import jieba
import requests
import json
from modules.tools.sdk import *
from modules.weather import *
from modules.baike import *

print('1、查询天气    2、百度百科')
print('3、新华字典    ')
功能 = input('输入你想使用的功能的序号:')
#b = jieba.lcut(a)

#天气
if 功能 == '1':
    city = input('输入地区:')
    if city:
        weather(city)
#百科
if 功能 == '2':
    try:
        q = input('输入查询的词语/其他:')
        print(q)
        print(baike(q))
    except:
        print('你真是难倒我了，求谅解嘤嘤嘤')

