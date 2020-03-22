import requests
from bs4 import BeautifulSoup
import lxml

def baidu_url(q,site=''):
    api = 'https://baidu.com/s?ie=UTF-8&wd='+q
    r = requests.get(api)
    r.encoding='utf-8'
    r = r.text
    #print(r)
    soup = BeautifulSoup(r,features='lxml')
    div = soup.find_all(name='div',attrs={"class":"result-op c-container xpath-log"})
    div = div[0].find_all(name='div',attrs={"class":"c-span18 c-span-last"})
    p = div[0].p
    p = str(p).replace('</p>','').replace('<p>','').replace(' ','')
    print(p)
baidu_url('晚安')
