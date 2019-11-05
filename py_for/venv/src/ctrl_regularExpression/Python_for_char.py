#定义字符类

import re
# p=r'[Jj]ava'
# m=re.search(p,'i like Java and Python')
# print(m)
# m=re.search(p,'i like JAVA and Python')
# print(m)
# m=re.search(p,'i like java and Python')
# print(m)

#字符类取反

# p=r'[^0123456789]' #或者  [^0-9]
# m=re.search(p,'1000')
# print(m)
# m=re.search(p,'Python 3')
# print(m)

#区间

# p1=r'[^A-Za-z0-9]'
# m1=re.search(p1,'Asdd1113340aa')
# print(m1)
#
# p2=r'[^0-25-7]'
# m2=re.search(p2,'888888')
# print(m2)

#预定义字符类

# p=r'[^0123456789]' #或者  [^0-9]
p=r'\D'
m=re.search(p,'1000')
print(m)
m=re.search(p,'Python 3')
print(m)
text='你们好Hello'
m=re.search(r'\w',text)
print(m)



