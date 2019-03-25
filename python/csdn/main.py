
import sys,threading,time
sys.path.append('./bin')

# from main_build import execute
from tou_config import climb

from main_build_thread import execute

climb['time_out'] = 5  #爬取时间 s
climb['speed_list'] = 1  #列表爬取速度 s
climb['speed_cont'] = 1  #内容爬取速度 s
climb['thread_list'] = 1 #列表页启动线程数 int
climb['thread_cont'] = 5  #内容页启动线程数 int
climb['save_db_time'] = 10  # 多长时间存储一次数据

# 执行
execute()
