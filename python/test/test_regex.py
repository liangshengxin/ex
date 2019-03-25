#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import re,json
# 正则匹配测试

files = open('./datas.txt','w+');
content = ''
r = requests.get('https://movie.douban.com/chart');

read = r.text
# files.seek(0,0)

# read = files.read();


pattern = re.compile('nbg"\shref="(.*?)"[\s\S]*?<img.*?src="(.*?)"[\s\S]*?pl2">\s*<a.+>\s*(.*)[\s\S]*?">(.*?)</span>',re.I|re.M)

result = pattern.findall(read)


for item in result:
    content+='链接地址:'+item[0]+'\r\n'
    content+='封面图片:'+item[1]+'\r\n'
    content+='标题:'+item[2]+' / '+item[3]+'\r\n'
    content+='-------------------------\r\n'


print(content)
# print(json.dumps(result))

files.write(content);
files.close()


