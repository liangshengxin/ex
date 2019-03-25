
import re,redis

#数据处理


class DataHandle:
    __config_save_db = None #数据处理配置 save_db
    __config_climb = None #爬取配置
    redis = None 
    # 初始化数据处理配置
    def __init__(self,tou_config):
        self.__config_save_db = tou_config.save_db
        self.__config_climb = tou_config.climb
        self.redis = redis.Redis(host=self.__config_save_db['redis_host'],port=self.__config_save_db['redis_port'])


    # ----------------
    # @param lists 获取的列表数据 get_content.GetContent().getList()
    # @return data 待存数据
    # @return url_list 内容页地址
    # ----------------
    def get_list(self,lists):
        data,url_list = self.__listData(lists)
        if len(data)>0:
            return data,url_list
        return False,False
    # ----------------
    # @param content 内容页数据 get_content.getContent.getFind(url)
    # @return string
    #-----------------
    def get_content(self,content):
        content = self.__findData(content)
        if not content:
            return False
        return content

    # 内容页url生成
    def get_content_url(self,item_id):
        return self.__config_climb['host']+item_id

    #内容页数据处理
    def __findData(self,content):
        if not isinstance(content,str):
            return False 
        pattern = re.compile(r'articleInfo:[\s\S]*?{[\s\S]*?content:\s\'([\s\S]*?)\'[\s\S]*?}',re.I|re.M)
        for item in pattern.findall(content):
            if not item:
                return False
            return item

    # 列表页数据处理
    def __listData(self,lists):
        datas = {}
        #内容页待爬列表
        url_list = {} 
        #验证数据是否为空
        if not lists:
            return False
        
        # 整理列表数据 
        for item in lists:
            field = self.__listField(item)
            if not field:
                continue
             # 唯一性
            if not self.__check_one(field['item_id']):
                continue
            datas[field['item_id']] = field
            url_list[field['item_id']] = self.get_content_url(field['item_id'])
        return datas,url_list
    
    # 唯一性检测
    # item_id 文章id
    # @return True唯一 | False不唯一
    def __check_one(self,item_id):
        if not self.redis.pfadd(self.__config_save_db['redis_check_itemid'],item_id):
            return False
        return True

    # 列表页单条信息处理
    def __listField(self,item):
        data={}
        dbc = self.__config_save_db
        # 单条列表数据
        for k,v in item.items():
            if not v:
                continue
            if(k in dbc['save_data_list']):
                # data[k] = v
                data[dbc['save_data_list'][k]] = v

        # 列表页数据完整性检查
        if dbc['check_data'] and (len(data)!=len(dbc['save_data_list'])):
            return False

        # 附加信息
        for key,val in dbc['save_data_define'].items():
            if isinstance(val,str):
                data[key] = val
            else:
                loadF = data[val['key']] #处理字段的值
                data[key] = val['method'](loadF)
        return data
