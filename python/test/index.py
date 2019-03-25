#!/usr/bin/python36
# -*- coding: UTF-8 -*-

# 爬今日头条热点

import re,requests,time,pymongo,redis
from bs4 import BeautifulSoup

# mongodb
myclient = pymongo.MongoClient("mongodb://192.168.44.137:27017")
mydb = myclient['toutiao']
tabs = mydb['tops']

#redis
redis = redis.Redis(host="127.0.0.1",port=6379)
listKey = "toutiao:set:"


# 数据记录
allCount = 0 #总爬区次数

#爬取速度 
outtime = 0.5 #几秒/1次
offtime = 5 #新数据为0时等待时间 秒

# 代理
# proxy = {
#     'http':'163.125.31.156:8118',
#     'http':'182.207.232.135:49166',
#     'http':'211.159.171.58:80',
#     'http':'125.123.138.86:9999',
#     'http':'182.92.113.148:8118',
#     'http':'222.189.191.88:9999',
# }

# 爬取数据 return request对象
def getPa(url):
    
    heads = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:65.0) Gecko/20100101 Firefox/65.0',
        'Host':'www.toutiao.com',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate, br',
        'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Cache-Control':'max-age=0',
        'Connection':'keep-alive',
        'TE':'Trailers',
        'Upgrade-Insecure-Requests':'1',
        'Cookie':'uuid="w:776b77018bf240808c686c8d0afcbd49"; _ga=GA1.2.776762302.1514380991; tt_webid=6663303340150294024; WEATHER_CITY=%E5%8C%97%E4%BA%AC; tt_webid=6663303340150294024; UM_distinctid=16937e9014f206-09dfcb14701a16-11666e4a-144000-16937e90150fe; CNZZDATA1259612802=1463985992-1551419514-https%253A%252F%252Fwww.baidu.com%252F%7C1551526286; csrftoken=68bbe601b5f823d7d363f59c18cae5f0; __tasessionId=suw3hc55w1551531580195',
    }
    cookie = {
        
    }
    # session = requests.Session()
    r = requests.get(url,headers=heads)
    
    return r

# 处理数据
def dataHandle():
    global allCount
    newCount = 0 
    datas = {}
    req = getPa('https://www.toutiao.com/api/pc/feed/?category=news_hot&utm_source=toutiao&widen=1&max_behot_time=0&max_behot_time_tmp=0&tadrequire=true&as=A1955C27EA372A5&cp=5C7A37727A15FE1&_signature=gnMM3AAA3hYLkjVG8ZAnfoJzDM')
    jsons = req.json()
    if len(jsons)<=0:
        return datas,0
    # print(jsons.get('data'))
    for item in jsons['data']:
        allCount+=1
        # datas += '标题：'+item.get('title')+'\n'
        # datas += 'id：'+item.get('item_id')+'\n'
        # datas += '图像地址：'+str(item.get('image_url'))+'\n'
        # datas +='------------------------------\r\n'
        item_id = item.get('item_id')
        image_url = str(item.get('image_url'))
        title = item.get('title')
        url = 'https://www.toutiao.com'+str(item.get('source_url'))

        checkId = redis.sadd(listKey,item_id)
        # 记录本次新记录数
        if checkId>0:
            newCount+=checkId
        else:
            continue

        # 整理数据
        datas[item_id] = {
            'item_id':item_id,
            'image_url':image_url,
            'title':title,
            'url':url,
        }
    return datas.values(),newCount




def main():
    while True:
        data,newCount = dataHandle()#整理后的数据
        sumCount = redis.scard(listKey) #获取新数据总量
        if newCount<=0:
            print('本次未获取到新数据；总的新数据：'+str(sumCount))
            time.sleep(offtime)
            continue

        tabs.insert_many(data) #插入数据库
        
        print('总爬取次数：'+str(allCount))
        print('本次获取新数据：'+str(newCount))
        print('总的新数据：'+str(sumCount))
        time.sleep(outtime)
    

main()

