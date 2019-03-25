

import time

# 请求头
headers = {
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


# 代理ip
proxy = {
    'http':'163.125.31.156:8118',
    'http':'182.207.232.135:49166',
    'http':'211.159.171.58:80',
    'http':'125.123.138.86:9999',
    'http':'182.92.113.148:8118',
    'http':'222.189.191.88:9999',
}



# 爬取配置
climb = {
        'time_out':3600, #爬取时间 s

        'speed_list':1, #列表爬取速度 s
        'speed_cont':1, #内容爬取速度 s

        #-[仅适用于多线程]-单位s-------------------------------
        'thread_list':1, #列表页启动线程数
        'thread_cont':1, #内容页启动线程数

        'block_list':5, #列表数据咱无时等待时间
        'block_time':0, #无需要获取的内容页数据时阻塞时间(0为阻塞直到有数据为止)
        'block_db_time':10, # 无待存储数据时等待时间

        'save_db_time':10, # 多长时间存储一次数据
        'save_db_count':500, #单次最大存储量
        #---------------------------------

        # True 开启代理 | False
        'proxy':False,
        # 请求地址 列表
        'url':'https://www.toutiao.com/api/pc/feed/?category=news_tech&utm_source=toutiao&widen=1&max_behot_time=0&max_behot_time_tmp=0&tadrequire=true&as=A105CCA75B5789D&cp=5C7B2778A9FD1E1&_signature=uHTOnwAA5B0xlfcFfbH2urh0zo',
        
        # 内容页地址
        'host':'https://www.toutiao.com/group/', #根域名和参数+item_id

        # 内容页附加请求头
        'headers_content':{
            'Referer':'https://www.toutiao.com/ch/news_tech/',
        },
        'headers_content_inde':None,
}

# 数据库配置
save_db = {
    'dbname':'toutiao', #数据库名称
    'dbtable':'article',#存入的表
    'dbhost':'127.0.0.1:27017', #地址
    'dbpass':'',#密码
    'dbuser':'',#用户名
    'redis_host':'127.0.0.1',
    'redis_port':'6379',
    'redis_check_itemid':'hyperloglog:itemid', #redis验证下标
    'check_data':True, #验证待存入数据是否完全 | False不验证


    #存入数据库（列表页）信息-----  爬取字段 : 数据库字段
    'save_data_list':{
        'item_id':'item_id', #信息id
        'title':'title', 
        'chinese_tag':'chinese_tag', #类别
        'source':'source',#发布人
        'media_avatar_url':'media_avatar_url',#发布人头像
        'image_url':'image_url',#图片地址
        'behot_time':'behot_time',#更新时间 时间戳
    },
    #存入数据库（内容页）信息
    'save_data_content':{
        'content':'content'
    },
    #存入数据库（附加）信息
    'save_data_define':{

        # 存入数据库的值 data_format  日期
        'data_format':{
            'key':'behot_time', #处理字段
            'method':lambda key:time.strftime("%Y-%m-%d",time.localtime(key)) #处理方法
        },
        # 时间
        'time_format':{
            'key':'behot_time', #处理字段
            'method':lambda key:time.strftime("%H:%M:%S",time.localtime(key))
        },
        # 直接给字段赋值
        'category':'1'
    }
}