n_list = []
# for i in range(10):
#     if i % 2 == 0:
#         n_list.append(i ** 3)
#n_list= [x ** 2   for x in range(10) if x % 2 == 0] #列表推导式
n_list = [x**2 for x in range(100) if x %2 ==0 if x % 5 ==0]
print(n_list)