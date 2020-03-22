百科关键字=['什么','意思','是']
def baike(q):
  import requests
  from bs4 import BeautifulSoup
  import lxml
  headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',}
  #请求URL并把结果用UTF-8编码
  #q = input('输入:')
  resp=requests.get('https://baike.baidu.com/item/'+q,headers=headers)
  resp.encoding = 'utf-8'
  resp = resp.text
  #print(resp)
  #使用BeautifulSoup去解析
  soup=BeautifulSoup(resp,"lxml")
  #print(soup)
  #获取所有以/wiki/开头的a标签的href属性
  listUrl=soup.findAll("div",{'class':'para'})
  #输出所有词条对应的名称和URL
  try:
    return listUrl[0].text
  except:
    return False
if (__name__ == '__main__'):
  print(baike(input('输入：')))
