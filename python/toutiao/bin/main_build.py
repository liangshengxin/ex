

import data_handle, get_content, tou_config, save_db
import time


get = get_content.GetContent(tou_config) #信息获取
dha = data_handle.DataHandle(tou_config) #信息处理
sdb = save_db.SaveDb(tou_config) #数据库操作



# ---------------------------
# 列表数据
# @return list_handle,list_url | False
# ---------------------------
def completed_list():
    list_data = get.getList() #获取列表信息
    if not list_data:
        return False,False
    print('成功抓取数据：'+str(len(list_data)))
    return dha.get_list(list_data) #处理列表数据
    

# ---------------------------
# 整合数据内容
# @ list_handle 列表处理后的数据
# @ list_url 也是列表处理后的数据
# @return整合后的内容 可直接使用sdb.saveAdd()存入数据库  |False
# ---------------------------
def completed_data(list_handle,list_url):
    for key,url in list_url.items():
        html = get.getFind(url) #内容信息
        content = dha.get_content(html) #处理内容信息
        # 判断是否有内容
        if not content:
            del list_handle[key]
            continue
        #存在则合并处理
        list_handle[key].update({'content':content})
        print('正在处理内容页数据：ID='+str(key))
        time.sleep(tou_config.climb['speed_cont'])
    if len(list_handle)>0:
        return list_handle.values()
    return False

# 存入数据库 直接使用 completed_data 方法返回的数据
# return num|False
def completed_db(data):
    request = sdb.saveAdd(data)
    if not request:
        return False
    return len(request.inserted_ids)




def execute_build():
    list_handle,list_url = completed_list()
    
    print('总爬次数：'+str(dha.redis.pfcount(tou_config.save_db['redis_check_itemid'])))

    if not list_handle:
        print('未获得符合条件数据')
        return False
    print('处理列表后剩余：'+str(len(list_url)))
    data = completed_data(list_handle,list_url)
    if not data:
        print('获取的数据均无内容')
        return False
    print('处理内容后剩余：'+str(len(data)))
    num=completed_db(data)
    if not num:
        print('插入数据库失败')
    print('插入成功：'+str(num))


def execute():
    while True:
        execute_build()
        time.sleep(tou_config.climb['speed_list'])    
    