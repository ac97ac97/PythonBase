import urllib.request
import hashlib
from bs4 import BeautifulSoup
import os
import re
import pymysql
url='https://www.nasdaq.com/symbol/aapl/historical#.UWdnJBDMhHk'

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

def validateUpdate(html):
    md5obj=hashlib.md5()
    # md5obj.update(html.encode(encoding='utf-8'))
    md5code=md5obj.hexdigest()
    print(md5code)

    old_md5code = ''
    f_name='md5.txt'

    if os.path.exists(f_name):
        with open(f_name,'r',encoding='utf-8') as f:
            old_md5code=f.read()

    if md5code == old_md5code:
        print('数据没有更新')
        return False
    else:
        with open(f_name,'w',encoding='utf-8') as f:
            f.write(md5code)
        print('数据更新')
        return True

req=urllib.request.Request(url)
with urllib.request.urlopen(req) as response:
    data=response.read()
    html=data.decode()
    sp=BeautifulSoup(html,'html.parser')

    div=sp.select('div#quotes_content_left_pnlAJAX')
    divstring = div[0]

    if validateUpdate(divstring):
        # pass
        trlist=sp.select('div#quotes_content_left_pnlAJAX table tbody tr')
        data = []
        for tr in trlist:
            trtext=tr.text.strip('\n\r')
            if trtext == '':
                continue

            rows = re.split(r'\s+',trtext)
            fields={}
            fields['Date']=rows[0]
            fields['Open'] = float(rows[1])
            fields['High'] = float(rows[2])
            fields['Low'] = float(rows[3])
            fields['Close'] = float(rows[4])
            fields['Volume'] = int(rows[5].replace(',',''))
            data.append(fields)

        print(data)

    for row in data:
        row['Symbol'] ='AAPL'
        insert_hisq_data(row)
