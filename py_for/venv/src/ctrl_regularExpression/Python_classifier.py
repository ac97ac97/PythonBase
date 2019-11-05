#量词的使用 d*/? 代表字符 d{*}代表数字
import re
# m=re.search(r'\d?','87654321')
# print(m)
#
# m=re.search(r'\d?','ABC')
# print(m)
#
# m=re.search(r'\d*','87654321')
# print(m)
#
#
# m=re.search(r'\d*','ABC')
# print(m)
#
#
# m=re.search(r'\d+','87654321')
# print(m)
#
# m=re.search(r'\d+','ABC')
# print(m)
#
# m=re.search(r'\d{8}','87654321')
# print(m)
#
# m=re.search(r'\d{8}','ABC')
# print(m)
#
# m=re.search(r'\d{7,8}','87654321')
# print(m)
#
# m=re.search(r'\d{9,}','87654321')
# print(m)

#贪婪量词和懒惰量词

m=re.search(r'\d{5,8}','87654321') #贪婪量词
print(m)

m=re.search(r'\d{5,8}?','87654321') #懒惰量词
print(m)




