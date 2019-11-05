import datetime
import hashlib
import logging
import os
import re
import threading
import time
import urllib.request
from bs4 import BeautifulSoup
import pymysql

def insert_hisq_data(row):
    # 建立数据库连接
    connection = pymysql.connect(host='localhost', user='root', password='root', database='nasdaq', charset='utf8')
    try:
        # 2创建游标对象
        with connection.cursor() as cursor:
            # 3 执行SQL操作
            sql = 'insert into historicalquote '\
                  '(HDate,Open,High,Low,Close,Volume,Symbol)' \
                  'values (%(Date)s,%(Open)s,%(High)s,%(Low)s,%(Close)s,%(Volume)s,%(Symbol)s)'

            affectedcount=cursor.execute(sql,row)

            print('影响数据的行数：{0}'.format(affectedcount))
            # 提交数据事务
            connection.commit()
        # with代码块结束 5关闭游标
    except pymysql.DatabaseError as error:
        # 4回滚数据库事务
        connection.rollback()
        print(error)
    finally:
        # 6关闭数据连接
        connection.close()

# logging.basicConfig(level=logging.INFO,format='%(asctime)s'-'%(threadName)s-'
#                                                '%(name)s'-'%(funcName)s'-'%(levelname)s'-'%(message)s')
logging.basicConfig(level=logging.INFO,format='%(asctime)s -%(threadName)s-'
                                               '%(name)s-%(funcName)s-%(levelname)s-%(message)s')

logger=logging.getLogger(__name__)
isrunning=True
interval=5
def controlthread_body():
    global interval,isrunning
    while isrunning:
        i=input('输入bye终止爬虫，输入数字改变爬虫的工作间隔，单位秒')
        logger.info('控制输入{0}'.format(i))
        try:
            interval=int(i)
        except ValueError:
            if i.lower() == 'bye':
                isrunning=False

def istradtime():
    now = datetime.datetime.now()
    df='%H%M%S'
    strnow=now.strftime(df)
    starttime=datetime.time(9,30).strftime(df)
    endtime = datetime.time(15, 30).strftime(df)

    if now.weekday() == 5 or now.weekday() == 6 or(strnow<starttime or strnow >endtime):
        return False
    return True

def workthread_body():
    global interval, isrunning

    while isrunning:
        if istradtime():
            logger.info('交易时间爬虫休眠1h')
            time.sleep(60*60)
            continue
        #...
        logger.info('爬虫开始工作')
        # ...
        logger.info('爬虫开休眠{0}秒'.format(interval))
        time.sleep(interval)

def main():
    global interval, isrunning

    workthread=threading.Thread(target=workthread_body,name='WorkThread')
    workthread.start()

    controlthread = threading.Thread(target=controlthread_body, name='ControlThread')
    controlthread.start()


if __name__ == '__main__':
    main()