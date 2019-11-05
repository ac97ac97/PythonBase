#断点为错误处 外部函数不能访问内部嵌套函数的局部变量
# def calculate(n1, n2, opr):
#     multiple = 2
#
#     def add(a, b):
#         return (a + b) * multiple
#
#     def sub(a, b):
#         return (a - b) * multiple
#
#     if opr == '+':
#         return add(n1 + n2)
#     else:
#         return sub(n1 - n2)
#
#
# print(calculate(10, 5, '+'))

#函数类型
# def calculate_fun(opr):
#
#     def add(a, b):
#         return (a + b)
#
#     def sub(a, b):
#         return (a - b)
#
#     if opr == '+':
#         return add
#     else:
#         return sub
# f1=calculate_fun('+')
# f2=calculate_fun('-')
# print(type(f1))
# print("10 + 5 = {0}".format(f1(10,5)))
# print("10 - 5 = {0}".format(f2(10,5)))

#函数重构
# def calculate_fun(opr):
#
#     if opr == '+':
#         return lambda a,b :(a+b)
#
#     else:
#         return lambda a,b:(a-b)
# f1=calculate_fun('+')
# f2=calculate_fun('-')
# print(type(f1))
# print("10 + 5 = {0}".format(f1(10,5)))
# print("10 - 5 = {0}".format(f2(10,5)))
#filter()函数的使用

# users=['zhangsan','lisi','wangwu','zhaoliu']
# userfilter=filter(lambda u:u.startswith('z'),users) #过滤以z开头的
# print(list(userfilter))

# number_list=range(1,11)
# numberFilter=filter(lambda it:it % 2 == 0,number_list) #过滤偶数
# print(list(numberFilter))

#map() 函数的使用

# users=['Zhangsan','Lisi','Wangwu','Zhaoliu']
# user_map=map(lambda u : u.lower(),users)
# print(list(user_map))

#map() + filter() 过滤出含Z的名字并把其转换为小写字母

# users=['Zhangsan','Lisi','Wangwu','Zhaoliu']
# user_filter=filter(lambda i :i.startswith('Z'),users)
# use_map=map(lambda u:u.lower(),user_filter)
# print(list(use_map))

#reduce() 函数的使用 聚合累计求和 若第四个参数不传入默认为0 传入则加入传参 与前面元组一起求和

from functools import reduce

a=(1,2,3,4)
#a_reduce=reduce(lambda acc,i :acc+i,a) #1
a_reduce=reduce(lambda acc,i :acc+i,a,2) #1
print(a_reduce)

