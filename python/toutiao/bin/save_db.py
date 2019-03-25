

import pymongo

# 存入数据库


class SaveDb:
    __config = None
    __mongo=None
    __table=None 

    # 初始配置
    def __init__(self,tou_config):
        self.__config = tou_config
        try:
            self.__mongo = pymongo.MongoClient('mongodb://'+self.__config.save_db['dbhost'])
        except:
            print('mongodb连接失败')
        database = self.__mongo[self.__config.save_db['dbname']]
        self.__table = database[self.__config.save_db['dbtable']]
    
    # --------------------
    # 存入数据库
    # param dists 字典类型 [{key:value},...]
    def saveAdd(self,dicts):
        if len(dicts)<=0:
            return False
        return self.__table.insert_many(dicts)
