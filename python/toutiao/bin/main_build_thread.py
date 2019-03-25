

# 多线程抓取

import data_handle, get_content, tou_config, save_db
import time,threading,json


get = get_content.GetContent(tou_config) #信息获取
dha = data_handle.DataHandle(tou_config) #信息处理
sdb = save_db.SaveDb(tou_config) #数据库操作



# 列表数据 key
redis_list_key = 'python:list:list'
# 待存数据库列表key
redis_cont_key = 'python:list:cont'


# ---------------------------
# 列表数据 同main_build 未有变更
# @return list_handle,list_url | False
# ---------------------------
def completed_list():
    list_data = get.getList() #获取列表信息
    if not list_data:
        return False,False
    print('成功抓取数据：'+str(len(list_data)))
    return dha.get_list(list_data) #处理列表数据
    


# 存入数据库
# return num|False
def completed_db(data):
    request = sdb.saveAdd(data)
    if not request:
        return False
    return len(request.inserted_ids)


# 待执行 -- 列表
def thread_list_build():
    list_handle,list_url = completed_list()
    if not list_handle:
        print('未获得符合条件的列表数据，剩余：'+str(dha.redis.llen(redis_list_key))+' 待处理')
        time.sleep(tou_config.climb['block_list'])
        return False
    # data存入redis列表
    for item in list_handle.values():
        dha.redis.rpush(redis_list_key,json.dumps(item))
    print('获取列表成功，剩余：'+str(dha.redis.llen(redis_list_key))+' 待处理')
    

# 待执行 -- 内容
def thread_cont_build():
    i_cont = dha.redis.blpop(redis_list_key,tou_config.climb['block_time'])
    if not i_cont:
        print('未从列表中获取数据！')
        return False
    items = json.loads(i_cont[1])
    url = dha.get_content_url(items['item_id']) #内容url
    html = get.getFind(url) #内容信息
    content = dha.get_content(html) #处理内容信息
    # 判断是否有内容
    if not content:
        print('未获取内容页数据：'+str(items['item_id'])+'-----page-----default')
        return False
    items.update({'content':content})
    dha.redis.rpush(redis_cont_key,json.dumps(items))
    # print('获取内容：'+str(items['item_id']))

def thread_list():
    timeEnd = time.time()+tou_config.climb['time_out']
    while True:
        thread_list_build()
        if timeEnd<time.time():
            break;

        time.sleep(tou_config.climb['speed_list'])

def thread_cont():
    timeEnd = time.time()+tou_config.climb['time_out']
    while True:
        thread_cont_build()
        if timeEnd<time.time():
            break;
        time.sleep(tou_config.climb['speed_cont'])

def thread_db():
    timeEnd = time.time()+tou_config.climb['time_out']
    while True:
        datas = []
        items = dha.redis.lrange(redis_cont_key,0,tou_config.climb['save_db_count'])
        dha.redis.ltrim(redis_cont_key,tou_config.climb['save_db_count'],-1)
        if not items:
            print('无待存数据-----save-----db：')

            if timeEnd<time.time():
                break;

            time.sleep(tou_config.climb['block_db_time'])
            continue
        for item in items:
            datas.append(json.loads(item))
        lens = completed_db(datas)
        print('已存入数据库-----save-----db：'+str(lens))

        if timeEnd<time.time():
            break;

        time.sleep(tou_config.climb['save_db_time'])


def execute_build():
    threads = []
    t_sum = t_list = tou_config.climb['thread_list']
    t_cont = tou_config.climb['thread_cont']
    if t_list<t_cont:t_sum=t_cont
    for i in range(t_sum):
        if t_list>0:
            threads.append(threading.Thread(target=thread_list))
        if t_cont>0:
            threads.append(threading.Thread(target=thread_cont))
        t_list-=1
        t_cont-=1
    threads.append(threading.Thread(target=thread_db))
    return threads

def execute():
    threads = execute_build()
    for thr in threads:
        thr.start()
    for thr in threads:
        thr.join()
    


