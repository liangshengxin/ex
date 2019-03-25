
import requests

# 数据获取


class GetContent:
    __config = None
    __proxy = {}
    # 数据抓取初始配置
    def __init__(self,tou_config):
        self.__config=tou_config
        if self.__config.climb['proxy']:
            self.__proxy = self.__config.proxy
    # ---------
    # 爬取列表页
    # return list|False
    # ---------
    def getList(self):
        url = self.__config.climb['url'] #地址
        try:
            r = requests.get(url,headers=self.__config.headers,proxies=self.__proxy)
            json_data = r.json()
            if self.__status(r.status_code) and self.__check(json_data):
                return json_data['data']
        except:
            print('列表爬取失败')
        return False

    # ---------
    # 爬取内容页
    # url 内容页地址
    # return html|False
    # ---------
    def getFind(self,url):
        if (self.__config.climb['headers_content_inde']) and len(self.__config.climb['headers_content_inde'])>0:
            headers = self.__config.climb['headers_content_inde']
        else:
            headers = self.__config.climb['headers_content']
            headers.update(self.__config.headers)
        try:
            r = requests.get(url,headers=headers,proxies=self.__proxy)
            if self.__status(r.status_code):
                return r.text
        except:
            print('内容爬取失败')
        return False


    # 验证数据
    def __check(self,dists):
        if len(dists)>0 and len(dists['data'])>0:
            return True
        return False

    # 验证抓取
    def __status(self,status_code):
        if status_code==200:
            return True
        return False