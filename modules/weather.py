import requests
import json

天气关键字 = ['天气','下雨','风级','','温度','几度']
def weather(city):
    api='http://wthrcdn.etouch.cn/weather_mini?city='+city
    r = requests.get(api)
    weather_dict=json.loads(r.text)
    forecast = weather_dict['data']['forecast']
    print('城市：',weather_dict.get('data').get('city'))
    print('温度：',weather_dict.get('data').get('wendu')+'℃ ')
    print('感冒：',weather_dict.get('data').get('ganmao'))
    print('风向：',forecast[0].get('fengxiang'))
    print('风级：',forecast[0].get('fengli'))
    print('高温：',forecast[0].get('high'))
    print('低温：',forecast[0].get('low'))
    print('天气：',forecast[0].get('type'))
    print('日期：',forecast[0].get('date'))
    print('*******************************')
    four_day_forecast =input('是否要显示未来四天天气，是/否：')
    if four_day_forecast == '是' or four_day_forecast =='Y' or four_day_forecast =='y':
        for i in range(1,5):
            print('日期：',forecast[i].get('date'))
            print('风向：',forecast[i].get('fengxiang'))
            print('风级：',forecast[i].get('fengli'))
            print('高温：',forecast[i].get('high'))
            print('低温：',forecast[i].get('low'))
            print('天气：',forecast[i].get('type'))
            print('--------------------------')
    print('***********************************')
