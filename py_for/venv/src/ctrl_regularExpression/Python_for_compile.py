import re

# 已编译正则表达式对象

# p=r'\w+@zhijieketang\.com'
# regex=re.compile(p)
#
# text="Tony's email is tony_guan588@zhijieketang.com."
# m=regex.search(text)
# print(m)
#
# m=regex.match(text)
# print(m)
#
# p=r'[Jj]ava'
# regex=re.compile(p)
# text='I like Java and java'
#
# match_list=regex.findall(text)
# print(match_list)
#
# match_iter=regex.finditer(text)
# for m in match_iter:
#     print(m.group())
#
# p=r'\d+'
# regex=re.compile(p)
# text='AB12CD34EF'
# clist=regex.split(text)
# print(clist)
#
# replace_text=regex.sub(' ',text)
# print(replace_text)

# 编译标志
#
# text='你们好Hello'
# p=r'\w+'
# regex=re.compile(p,re.U)
# m=regex.search(text)
# print(m)
# m=regex.match(text)
# print(m)
# regex=re.compile(p,re.A)
# m=regex.search(text)
# print(m)
# m=regex.match(text)
# print(m)

# 忽略大小写
# p=r'(java).*(python)'
# regex=re.compile(p,re.I)
#
# m=regex.search('i like Java and Python')
# print(m)
# m=regex.search('i like JAVA and Python')
# print(m)
# m=regex.search('i like java and Python')
# print(m)

# 点元字符匹配换行符
# p=r'.+'
# regex=re.compile(p)
# m=regex.search('Hello\nWorld')
# print(m)
# regex=re.compile(p,re.DOTALL)
# m=regex.search('Hello\nWorld')
# print(m)

# 多行模式
# p=r'^World'
# regex=re.compile(p)
# m=regex.search('Hello\nWorld')
# print(m)
# regex=re.compile(p,re.M)
# m=regex.search('Hello\nWorld')
# print(m)

# 详细模式

p = """(java) #匹配Java字符串
.*            #匹配任意字符零或多个
(python)      #匹配Python字符串
"""

regex = re.compile(p, re.I | re.VERBOSE)

m = regex.search('i like Java and Python')
print(m)
m = regex.search('i like JAVA and Python')
print(m)
m = regex.search('i like java and Python')
print(m)
