import pymysql

"""有条件查询"""

# # 1.建立数据库连接 提取多条数据
# connection = pymysql.connect(
#     host='localhost',
#     user='root',
#     password='root',
#     database='MyDB',
#     charset='utf8'
#
# )
# try:
#     # 2.创建游标对象
#     with connection.cursor() as cursor:
#         # 3.执行SQL操作
#         # sql='select name,userid from user where userid >%(id)s'
#         # cursor.execute(sql,[0]) cursor.execute(sql,0)
#         sql = 'select name,userid from user where userid >%(id)s'
#         cursor.execute(sql, {'id':0})
#         # 4.提取结果集
#         result_set = cursor.fetchall()
#         for row in result_set:
#             print('id:{0} -name:{1} '.format(row[1], row[0]))
#         # with代码块结束5. 结束光标
# finally:
#     # 6.关闭数据连接
#     connection.close()

"""无条件查询"""

# 1.建立数据库连接  提取一条数据
# connection = pymysql.connect(
#     host='localhost',
#     user='root',
#     password='root',
#     database='MyDB',
#     charset='utf8'
#
# )
# try:
#     # 2.创建游标对象
#     with connection.cursor() as cursor:
#         # 3.执行SQL操作
#         # sql='select name,userid from user where userid >%(id)s'
#         # cursor.execute(sql,[0]) cursor.execute(sql,0)
#         sql = 'select max(userid) from user'
#         cursor.execute(sql)
#         # 4.提取结果集
#         row = cursor.fetchone()
#         if row is not None:
#             print('最大用户Id:{0}'.format((row[0])))
#         # with代码块结束5. 结束光标
# finally:
#     # 6.关闭数据连接
#     connection.close()

"""数据插入"""


# 查询最大的用户Id
# def read_max_userid():
#
#
# # <省略最大的用户id代码>
#
# # 建立数据库连接
#   connection = pymysql.connect(host='localhost', user='root', password='root', database='MyDB', charset='utf8')
# # 查询最大值
# maxid = read_max_userid()
# try:
#     # 2创建游标对象
#     with connection.cursor() as cursor:
#         # 3 执行SQL操作
#         sql = 'insert into user (useid,name) values (%s,%s)'
#         nextid = maxid + 1
#         name = 'Tony' + str(nextid)
#         cursor.execute(sql, (nextid, name))
#         print('影响数据的行数：{0}'.format(affectedcount))
#         # 提交数据事务
#         connection.commit()
#     # with代码块结束 5关闭游标
# except pymysql.DatabaseError:
#     # 4回滚数据库事务
#     connection.rollback()
# finally:
#     # 6关闭数据连接
#     connection.close()


"""数据更新"""


# 查询最大的用户Id



# 建立数据库连接
#   connection = pymysql.connect(host='localhost', user='root', password='root', database='MyDB', charset='utf8')
# 查询最大值
# maxid = read_max_userid()
# try:
#     # 2创建游标对象
#     with connection.cursor() as cursor:
#         # 3 执行SQL操作
#         sql = 'update user set name = %s where userid > %s'
#         affectedcount=cursor.execute(sql,('Tom',2))
#         print('影响数据的行数：{0}'.format(affectedcount))
#         # 提交数据事务
#         connection.commit()
#     # with代码块结束 5关闭游标
# except pymysql.DatabaseError:
#     # 4回滚数据库事务
#     connection.rollback()
#     print(e)
# finally:
#     # 6关闭数据连接
#     connection.close()


"""数据删除"""


# 查询最大的用户Id
def read_max_userid():


# <省略最大的用户id代码>

# 建立数据库连接
  connection = pymysql.connect(host='localhost', user='root', password='root', database='MyDB', charset='utf8')
# 查询最大值
maxid = read_max_userid()
try:
    # 2创建游标对象
    with connection.cursor() as cursor:
        # 3 执行SQL操作
        sql = 'delete from user  where userid = %s'
        affectedcount=cursor.execute(sql,maxid)
        print('影响数据的行数：{0}'.format(affectedcount))
        # 提交数据事务
        connection.commit()
    # with代码块结束 5关闭游标
except pymysql.DatabaseError:
    # 4回滚数据库事务
    connection.rollback()
finally:
    # 6关闭数据连接
    connection.close()
