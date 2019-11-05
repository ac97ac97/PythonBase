import re
#search()和match()函数

# p=r'\w+@zhijieketang\.com'
# text="Tony's email is tony_guan588@zhijieketang.com."
# m=re.search(p,text)
# print(m)
#
# m=re.match(p,text)
# print(m)
#
# email='tony_guan588@zhijieketang.com'
# m=re.search(p,email)
# print(m)
#
# m=re.search(p,email)
# print(m)
#
# #match对象的几个方法
# print('match对象的几个方法')
# print(m.group())
# print(m.start())
# print(m.end())
# print(m.span())

#findall()和finditer()函数

# p=r'[Jj]ava'
# text='I like Java and java'
# math_list = re.findall(p,text)
# print(math_list)
# math_iter=re.finditer(p,text)
# for m in math_iter:
#     print(m.group())

#字符串的分割

# p=r'\d+'
# text='AB12CD34EF'
# clist=re.split(p,text)
# print(clist)
#
# clist=re.split(p,text,maxsplit=1)
# print(clist)
#
# clist=re.split(p,text,maxsplit=2)
# print(clist)

#字符串分割

p=r'\d+'
text='AB12CD34EF'

replace_text=re.sub(p,' ',text)
print(replace_text)

replace_text=re.sub(p,' ',text,count=1)
print(replace_text)

replace_text=re.sub(p,' ',text,count=2)
print(replace_text)