import re

p1 = r'\w+@zhijieketang\.com'
p2 = r'^\w+@zhijieketang\.com$'
text = "Tony 's email is tony_guan5588@zhijieketang.com"
m = re.search(p1, text)
print(m)
m = re.search(p2, text)
print(m)
email = "tony_guan5588@zhijieketang.com"
m = re.search(p2, email)
print(m)
