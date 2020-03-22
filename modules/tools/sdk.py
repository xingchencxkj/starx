import json

def 查询关键字(关键字列表,输入):
    for i in 关键字列表:
        if i in 输入:
            return True
    return False 

def 获取地区(sentence):
    f=open('citydata.json','r').read()
    citydata=json.loads(f)
    for data in sentence:
        for i1 in citydata:
            if i1['name']==data:
                if '省' in data:
                    return data.split('省')[0]
                else:
                    return data.split('市')[0]
            if i1['name']==data+'市':
                return data
            if i1['name']==data+'省':
                return data
            ###省级分割线###
            for i in i1['cityList']:
                if i['name']==data:
                    if '市' in data:
                        return data.split('市')[0]
                    else:
                        return data.split('区')[0]
                if i['name']==data+'区':
                    return data
                if i['name']==data+'市':
                    return data
            ###市级分割线###
                for j in i['countyList']:
                    if j['name']==data:
                        return data.split('区')[0]
                    if j['name']==data+'区':
                        return data
    return False
