
# 单页面抓取  糗事百科

import requests,re,time
from bs4 import BeautifulSoup


listId = []   # 抓过的id存入列表
newCount = 0;   # 抓取新数据个数
sumCount = 0;   # 总抓取个数
newCountSum = 0; #新数据总数量



# i=0
# while i<10:
#     i=i+1
#     print(i)
#     time.sleep(0.2)




# 【页面抓取】------------
def getPa():
    r = requests.get('https://www.qiushibaike.com/text/');
    text = r.text
    # with open('./datas.txt','r') as op:
    #     text = op.read()
    return text

# [数据处理]-------------------
def dataHandle(html):
    datas = ''
    global listId,newCount,sumCount
    soup = BeautifulSoup(html,'lxml')

    regHtml = soup(id=True,class_=re.compile('^article block untagged'))

    for item in regHtml:
        id = item['id']
        sumCount+=1
        if listId.count(id):
            continue
        listId.append(item['id'])

        username = item.h2.get_text(strip=True) #用户名
        content = item.find(class_="content").get_text(strip=True) #内容
        statsVote = item.find(class_="stats-vote").get_text(strip=True)  #笑脸数
        statsComm = item.find(id=True,class_="qiushi_comments").get_text(strip=True) #评论量

        datas += '【用户id】:'+id+'\n'
        datas += '【用户名称】:'+content+'\n'
        datas += '【笑脸数】:'+statsVote+'\n'
        datas += '【评论量】:'+statsComm+'\n'
        datas += '---------------------------\r\n'
        
        newCount+=1
    return datas

def binds():
    text = getPa()
    datas = dataHandle(text)
    with open('./qiushi.txt','a+') as op:
        op.write(datas)



def main():
    global newCount,sumCount,newCountSum
    outTime = 60    #抓取新数据过少的等待秒数
    while True:
        binds()
        if(newCount>10):
            outTime=1
        else:
            outTime=60
        print('本次获取新数据：'+str(newCount))
        print('总数据：'+str(sumCount))
        newCountSum+=newCount
        print('新数据总数量：'+str(newCountSum))
        print('-------------------')
        newCount=0 #清空本次新数据
        time.sleep(outTime)
    


main()

    
    


