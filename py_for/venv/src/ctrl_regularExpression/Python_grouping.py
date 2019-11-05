import re
#分组的使用
# p=r'(121){2}'
# m=re.search(p,'1212134avxs')
# print(m)
# print(m.group())
# print(m.group(1))
#
# p=r'(\d{3,4})-d{3,4})'
# m=re.search(p,'00-19992313')
# print(m)
# print(m.group())
# print(m.groups())

#分组命名

# p=r'(?P<area_code>\d{3,4})-(?P<phone_code>\d{7,8})'
# m=re.search(p,'010-87654321')
# print(m)         #匹配
# print(m.group())  #返回匹配字符串
# print(m.groups()) #获得所有组内容
#
# #通过组编号返回组内容
# print(m.group(1))
# print(m.group(2))
#
# #通过组名返回组内容
#
# print(m.group('area_code'))
# print(m.group('phone_code'))

#反向引用分组
# p=r'<([\w]+)>.*</([\w]+)>'
# m=re.search(p,'<a>abc</a>')
# print(m)
# m=re.search(p,'<a>abc</b>')
# print(m)

# p=r'<([\w]+)>.*</\1>'
#
# m=re.search(p,'<a>abc</a>')
# print(m)
#
# m=re.search(p,'<a>abc</b>')
# print(m)

#非捕获字符

s='img1.jpg,img2.jpg,img3.bmp'

#捕获分组
p=r'\w+(\.jpg)'
mList=re.findall(p,s)
print(mList)

#非捕获分组

p=r'\w+(?:\.jpg)'
mList=re.findall(p,s)
print(mList)