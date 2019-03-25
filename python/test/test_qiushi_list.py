# 爬糗事百科列表


import re,requests,time,json
from bs4 import  BeautifulSoup

listId = [] #id列表
sumInt = 0  #记录总数量
newInt = 0  #记录新数据总数量

# 访问地址获取数据
def getPa(http):
    r = requests.get(http)
    if r.status_code==200:
        return r.text
    return False

def dataHandle(html):
    global listId,sumInt,newInt
    newCount=0
    data = {}
    soup = BeautifulSoup(html,'lxml')
    resList = soup(id=True,class_=re.compile('^article block untagged'))
    for item in resList:
        sumInt+=1
        readid = item['id']
        if listId.count(readid):
            continue
    
        username = item.find(class_="author clearfix").h2.get_text(strip=True)
        content = item.find(class_="content").get_text(strip=True)
        data[readid] = {
            'id':readid,
            'username':username,
            'content':content,
            
        }
        listId.append(readid)
        newInt+=1
        newCount+=1
    return data,newCount

def main():
    i=1 #初始页
    while True:
        pagelist = 'https://www.qiushibaike.com/text/page/'+str(i) #列表页
        html = getPa(pagelist) #获取数据
        
        if(not html):
            print('获取失败')
            break

        data,newCount = dataHandle(html) #提取数据
        dbAdd(data) #存储数据
        i+=1 #下一页
        print('当前列表：'+pagelist)
        print('最新数据：'+str(newCount))
        print('总爬条数：'+str(sumInt))
        print('总新数据：'+str(newInt))

        if(newCount<=0):
            i=1

        #新数据过少30秒执行一次
        if(newCount<10):
            time.sleep(30)
        time.sleep(0.5) #五秒执行一次

        # 页数爬完后初始页数从新开始
        
        


# 存储
def dbAdd(data):
    text = ''
    for key,item in data.items():
        text+='id：'+str(item['id'])+'\n'
        text+='用户名：'+item['username']+'\n'
        text+='内容：'+item['content']+'\n'
        text+='----------------------\r\n'
    with open('qiushi_list.txt','a+') as op:
        op.write(text)





main()
