# 单捕获处理异常

# import datetime as dt
# def read_date(in_date):
#     try:
#         date=dt.datetime.strptime(in_date,'%Y-%m-%d')  #跑出异常
#         return date
#     except ValueError as e:        #捕获产生的异常
#         print('处理ValueError异常')
#         print(e) #打印异常对象的输出信息
# str_date='201B-10-01'
# print('日期 = {0}'.format(read_date(str_date)))

# 多捕获处理异常 当一个except捕获一个异常其他模块将不会再其捕获异常 顺序 从上往下 先捕获子类后父类

# import datetime as dt
# def read_date_from_file(filename):
#     try:
#         file=open(filename)
#         in_date=file.read()
#         in_date=in_date.strip()#去除空白字符
#         date=dt.datetime.strptime(in_date,'%Y-%m-%d')#可能抛出ValueError异常
#         return date
#     except ValueError as e:
#         print('处理ValueError异常')
#         print(e)
#     except FileNotFoundError as e:
#         print('处理FileNotFoundError异常')
#         print(e)
#     except OSError as e:
#         print('处理OSError异常')
#         print(e)
# date=read_date_from_file('readme.txt')
# print('日期 = {0}'.format(date))

# OSError FileNotFoundError 调换顺序

# import datetime as dt
# def read_date_from_file(filename):
#     try:
#         file=open(filename)
#         in_date=file.read()
#         in_date=in_date.strip()#去除空白字符
#         date=dt.datetime.strptime(in_date,'%Y-%m-%d')#可能抛出ValueError异常
#         return date
#     except ValueError as e:
#         print('处理ValueError异常')
#         print(e)
#     except OSError as e:
#         print('处理OSError异常')
#         print(e)
#     except FileNotFoundError as e:
#         print('处理FileNotFoundError异常')
#         print(e)
#
# date=read_date_from_file('readme.txt')
# print('日期 = {0}'.format(date))

# try-except语句嵌套

# import datetime as dt
# def read_date_from_file(filename):
#     try:
#         file=open(filename)
#         try:
#           in_date=file.read()
#           in_date=in_date.strip()#去除空白字符
#           date=dt.datetime.strptime(in_date,'%Y-%m-%d')#可能抛出ValueError异常
#           return date
#         except ValueError as e:
#           print('处理ValueError异常')
#           print(e)
#     except FileNotFoundError as e:
#         print('处理FileNotFoundError异常')
#         print(e)
#     except OSError as e:
#         print('处理OSError异常')
#         print(e)
# date=read_date_from_file('readme.txt')
# print('日期 = {0}'.format(date))


# 多重捕获  若某个异常属于某个异常的子类只需捕获他的父类即可捕获其所有的子类

# import datetime as dt
# def read_date_from_file(filename):
#     try:
#         file=open(filename)
#         in_date=file.read()
#         in_date=in_date.strip()#去除空白字符
#         date=dt.datetime.strptime(in_date,'%Y-%m-%d')#可能抛出ValueError异常
#         return date
#     except (ValueError,OSError) as e:
#         print('调用处理method1方法处理...')
#         print(e)
#
# date=read_date_from_file('readme.txt')
# print('日期 = {0}'.format(date))

# 异常堆栈跟踪  traceback.print_exc(lirnit=None ,  flle=None ,  chain=True)

# import datetime as dt
# import traceback as tb
# def read_date_from_file(filename):
#     try:
#         file=open(filename)
#         in_date=file.read()
#         in_date=in_date.strip()#去除空白字符
#         date=dt.datetime.strptime(in_date,'%Y-%m-%d')#可能抛出ValueError异常
#         return date
#     except (ValueError,OSError) as e:
#         print('调用处理method1方法处理...')
#         tb.print_exc()
#
# date=read_date_from_file('readme.txt')
# print('日期 = {0}'.format(date))

# f i n a l l y 释放资源模块

# import datetime as dt
# def read_date_from_file(filename):
#     try:
#         file=open(filename)
#         in_date=file.read()
#         in_date=in_date.strip()#去除空白字符
#         date=dt.datetime.strptime(in_date,'%Y-%m-%d')#可能抛出ValueError异常
#         return date
#     except ValueError as e:
#         print('处理ValueError异常')
#         print(e)
#     except FileNotFoundError as e:
#         print('处理FileNotFoundError异常')
#         print(e)
#     except OSError as e:
#         print('处理OSError异常')
#         print(e)
#     finally:
#         file.close()
# date=read_date_from_file('readme.txt')
# print('日期 = {0}'.format(date))

# else模块

# import datetime as dt
#
#
# def read_date_from_file(filename):
#     try:
#         file = open(filename)
#     except OSError as e:
#         print('打开文件失败')
#     else:
#         print('打开文件成功')
#         try:
#             in_date = file.read()
#             in_date = in_date.strip()  # 去除空白字符
#             date = dt.datetime.strptime(in_date, '%Y-%m-%d')  # 可能抛出ValueError异常
#             return date
#         except ValueError as e:
#             print('处理ValueError异常')
#
#         except FileNotFoundError as e:
#             print('处理FileNotFoundError异常')
#
#         except OSError as e:
#             print('处理OSError异常')
#
#         finally:
#             file.close()
#
#
# date = read_date_from_file('readme.txt')
# print('日期 = {0}'.format(date))

# with as 代码块自动管理模块   完成后自动释放资源 不需要final 模块 不需要自己释放资源

# import datetime as dt
#
#
# def read_date_from_file(filename):
#     try:
#         # file=open(filename)
#         with open(filename) as file:
#             in_date = file.read()
#         in_date = in_date.strip()  # 去除空白字符
#         date = dt.datetime.strptime(in_date, '%Y-%m-%d')  # 可能抛出ValueError异常
#         return date
#     except ValueError as e:
#         print('处理ValueError异常')
#     except FileNotFoundError as e:
#         print('处理FileNotFoundError异常')
#     except OSError as e:
#         print('处理OSError异常')
#
#
# date = read_date_from_file('readme.txt')
# print('日期 = {0}'.format(date))

# 自定义异常类

# class MyException(Exception):
#     def __init__(self,message):
#         super.__init__(message)

# 显示抛出异常

import datetime as dt


class MyException(Exception):
    def __init__(self, message):
        super.__init__(message)


def read_date_from_file(filename):
    try:
        file = open(filename)
        in_date = file.read()
        in_date = in_date.strip()  # 去除空白字符
        date = dt.datetime.strptime(in_date, '%Y-%m-%d')  # 可能抛出ValueError异常
        return date
    except ValueError as e:
        raise MyException('不是有效的日期')
    except FileNotFoundError as e:
        raise MyException('文件找不到')
    except OSError as e:
        raise MyException('文件无法打开或者无法读取')


date = read_date_from_file('readme.txt')
print('日期 = {0}'.format(date))
