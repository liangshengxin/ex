

import time

# 请求头
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:65.0) Gecko/20100101 Firefox/65.0',
    'Host':'www.csdn.net',
    'Accept':'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Connection':'keep-alive',
    'Cookie':'Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1552921282,1552972152,1552972172,1553003445; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216000f45c9a449-02bdc0049b9535-12676c4a-1327104-16000f45c9b337%22%2C%22%24device_id%22%3A%2216000f45c9a449-02bdc0049b9535-12676c4a-1327104-16000f45c9b337%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; kd_user_id=97f39a1b-497f-4ad9-a5f0-4735061f62e0; Hm_ct_6bcd52f51e9b3dce32bec4a3997715ac=1788*1*PC_VC!5744*1*Yohoxx!6525*1*10_37329376190-1543042215403-301114; smidV2=20180512003735fdf7a8135898152cb19897220d0a73d700ba4fff84f3630f0; ARK_ID=JS15859053a9a676a476bf151e017958781585; _ga=GA1.2.915288253.1541663820; ADHOC_MEMBERSHIP_CLIENT_ID1.0=f32de0bd-e5da-be89-559e-e9764a4c75d5; UM_distinctid=16736981c270-07675bc8a14a0e-1160684a-144000-16736981c2874; uuid_tt_dd=10_37329376190-1543042215403-301114; UN=Yohoxx; BT=1551150520422; UserName=Yohoxx; UserInfo=d970f131398841838d8ccf4aed7f9ec7; UserToken=d970f131398841838d8ccf4aed7f9ec7; UserNick=Yohoxx; AU=DD8; dc_session_id=10_1548127815714.515518; TY_SESSION_ID=61ca6663-37f2-45a8-b6b7-21635fb5a54b; Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac=1553003507; aliyun_webUmidToken=TCB39715FF0AFDD27E1B8EC7E59C50975F559E8C2E4DEE7788303764C89; aliyun_UAToken=115#1XDJ1f1O1Ta0EMVnTCCf1CsoaTCGBJA1Q02mOCkwRCOccUNCjO0SI1tupXb5yzUc9jfPeK69tMNQi/JJhUU8AWCcZTBXurrQOSAyeKT8G6KdiQJRHZPhX21VaLBfDzFQOSfyeKT8uWNIi/JJhUU4AkNcaTBXs6/alYl+XHsHBXKp95TsMJaMSBWWnMA/wZssorHxEoGx3Yn6j5awQ1nIpm441I5Ryb4C2DkUhDEXXm/fytqHPsSfrm6EYzmYsPDMKkSiS/2tFWeDJUWx3+UmDmoI9rzhqw8erEylqyk1GgHNHJXlNt+p4UiYvcIKSFqNMYSavYeYXnZvF1ZMc8lDCQ577Hre1zI8YkIEyOcolmYsjXt5MlJH7gQev+t2YouzJw4vL40Zqqy0QUFpcROlWqN8PZwkecCarqYFemKE5SJLjCQ44UoB0V6mEasjp+pZWzwGxQYON9BAtN3g+MDvd++vqt6vT97jP/ALYpfXhqLqyRG8C6yCOll0F78IELJp+YDkzHksdMT6BG/oDXPz3kgLtkBJnrASiXoqLrdKjYuum6wl8Ljrl/DGJf7W3TmK1pDHzPcrkmdSzi4MD56y5t4MZBfdVtCOGQ4OL1mdRGQ8ZLMkv/+Md0qx+FBwMXadAqK769LV0QbBc0h/GWs6IjRQ05K9UKo7+BXSfANSfgggMVrhmgwMkV4Fs+76fNStzFSnng+Rx9KZp9YLDNcmsZDzZvin01==; yidun_tocken=9ca17ae2e6ffcda170e2e6eed2f7678cb8aabbbb7a86928fa6d15e838a8b84f761b5f0fad2f74d96868bb2f92af0feaec3b92a8f8fa08dae54868897aec85f828a9ba2d45aa8e70099ef21f4ac89b3d53babeaee9e; SESSION=c790dda7-0d1c-4bcb-a076-f39bf7cc0dc1; dc_tos=pom96c',
    'X-Requested-With':'XMLHttpRequest',
    'X-Tingyun-Id':'wl4EtIR_7Is;r=3729313',
    'TE':'Trailers',
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
        'block_db_time':20, # 无待存储数据时等待时间

        'save_db_time':10, # 多长时间存储一次数据
        'save_db_count':500, #单次最大存储量
        #---------------------------------

        # True 开启代理 | False
        'proxy':False,
        # 请求地址 列表
        'url':'https://www.csdn.net/api/articles?type=new&category=home',
        
        # 内容页地址
        'host':'https://blog.csdn.net/', #+ 发布人user_name + /article/details/ +信息id item_id

        # 内容页附加请求头
        'headers_content':{},
        # 内容页独立header头 设置后 附加和公共的header失效
        'headers_content_inde':{
            'Host':'blog.csdn.net',
            'Cache-Control':'max-age=0',
            'Upgrade-Insecure-Requests':'1',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:65.0) Gecko/20100101 Firefox/65.0',
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Cookie':'Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1552921282,1552972152,1552972172,1553003445; bdshare_firstime=1511439543644; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216000f45c9a449-02bdc0049b9535-12676c4a-1327104-16000f45c9b337%22%2C%22%24device_id%22%3A%2216000f45c9a449-02bdc0049b9535-12676c4a-1327104-16000f45c9b337%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; kd_user_id=97f39a1b-497f-4ad9-a5f0-4735061f62e0; Hm_ct_6bcd52f51e9b3dce32bec4a3997715ac=1788*1*PC_VC!5744*1*Yohoxx!6525*1*10_37329376190-1543042215403-301114; smidV2=20180512003735fdf7a8135898152cb19897220d0a73d700ba4fff84f3630f0; ARK_ID=JS15859053a9a676a476bf151e017958781585; _ga=GA1.2.915288253.1541663820; ADHOC_MEMBERSHIP_CLIENT_ID1.0=f7b042a1-eb95-4c34-dd1b-5e815fdefc35; UM_distinctid=16736981c270-07675bc8a14a0e-1160684a-144000-16736981c2874; uuid_tt_dd=10_37329376190-1543042215403-301114; __yadk_uid=YrSrQL5Rlx3dJQfcpdHHOZDZ18Kwvlo1; UN=Yohoxx; BT=1551150520422; UserName=Yohoxx; UserInfo=d970f131398841838d8ccf4aed7f9ec7; UserToken=d970f131398841838d8ccf4aed7f9ec7; UserNick=Yohoxx; AU=DD8; dc_session_id=10_1548127815714.515518; Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac=1553014002; aliyun_webUmidToken=TCB39715FF0AFDD27E1B8EC7E59C50975F559E8C2E4DEE7788303764C89; aliyun_UAToken=115#1XDJ1f1O1Ta0EMVnTCCf1CsoaTCGBJA1Q02mOCkwRCOccUNCjO0SI1tupXb5yzUc9jfPeK69tMNQi/JJhUU8AWCcZTBXurrQOSAyeKT8G6KdiQJRHZPhX21VaLBfDzFQOSfyeKT8uWNIi/JJhUU4AkNcaTBXs6/alYl+XHsHBXKp95TsMJaMSBWWnMA/wZssorHxEoGx3Yn6j5awQ1nIpm441I5Ryb4C2DkUhDEXXm/fytqHPsSfrm6EYzmYsPDMKkSiS/2tFWeDJUWx3+UmDmoI9rzhqw8erEylqyk1GgHNHJXlNt+p4UiYvcIKSFqNMYSavYeYXnZvF1ZMc8lDCQ577Hre1zI8YkIEyOcolmYsjXt5MlJH7gQev+t2YouzJw4vL40Zqqy0QUFpcROlWqN8PZwkecCarqYFemKE5SJLjCQ44UoB0V6mEasjp+pZWzwGxQYON9BAtN3g+MDvd++vqt6vT97jP/ALYpfXhqLqyRG8C6yCOll0F78IELJp+YDkzHksdMT6BG/oDXPz3kgLtkBJnrASiXoqLrdKjYuum6wl8Ljrl/DGJf7W3TmK1pDHzPcrkmdSzi4MD56y5t4MZBfdVtCOGQ4OL1mdRGQ8ZLMkv/+Md0qx+FBwMXadAqK769LV0QbBc0h/GWs6IjRQ05K9UKo7+BXSfANSfgggMVrhmgwMkV4Fs+76fNStzFSnng+Rx9KZp9YLDNcmsZDzZvin01==; yidun_tocken=9ca17ae2e6ffcda170e2e6eed2f7678cb8aabbbb7a86928fa6d15e838a8b84f761b5f0fad2f74d96868bb2f92af0feaec3b92a8f8fa08dae54868897aec85f828a9ba2d45aa8e70099ef21f4ac89b3d53babeaee9e; SESSION=c790dda7-0d1c-4bcb-a076-f39bf7cc0dc1; dc_tos=pomh9u; firstDie=1; TY_SESSION_ID=c61a5e1a-3776-4c18-b658-2825f037a91b',
        }
}

# 数据库配置
save_db = {
    'dbname':'csdn', #数据库名称
    'dbtable':'article',#存入的表
    'dbhost':'127.0.0.1:27017', #地址
    'dbpass':'',#密码
    'dbuser':'',#用户名
    'redis_host':'127.0.0.1',
    'redis_port':'6379',
    'redis_check_itemid':'hyperloglog:csdn:itemid:', #redis验证下标
    'check_data':True, #验证待存入数据是否完全 | False不验证


    #存入数据库（列表页）信息----- 爬取字段  : 数据库字段  
    'save_data_list':{
        'id':'item_id', #信息id
        'title':'title',
        'category':'chinese_tag', #类别名称
        'nickname':'source',#发布人昵称
        'user_name':'user_name', #发布人
        'avatar':'media_avatar_url',#发布人头像
        'shown_time':'behot_time',#更新时间 时间戳
        'summary':'summary', #概要
    },
    #存入数据库（内容页）信息
    'save_data_content':{
        'content':'content'
    },
    #存入数据库（附加）信息
    'save_data_define':{

        # 存入数据库的字段 data_format  日期
        'data_format':{
            'key':'behot_time', #处理字段（数据库字段）
            'method':lambda key:time.strftime("%Y-%m-%d",time.localtime(key)) #处理方法
        },
        # 时间
        'time_format':{
            'key':'behot_time', #处理字段
            'method':lambda key:time.strftime("%H:%M:%S",time.localtime(key))
        },
        'summary':{
            'key':'summary',
            'method':lambda str:str[0:200]
        },
        # 直接给字段赋值
        'category':'2'
    }
}