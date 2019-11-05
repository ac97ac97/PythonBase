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



