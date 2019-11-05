#random模块
import random
# 0.0 --- 1.0 random
# print('0.0 --- 1.0 random')
# for i in range(0,10):
#     x=random.random()
#     print(x)

# 0.0 --- 5.0 random
# print('0.0 --- 5.0 random')
# for i in range(0,10):
#     x=random.randrange(5)
#     print(x,end=' ')


# 5.0 --- 10.0 random 不包括10
# print('0.0 --- 5.0 random')
# for i in range(0,10):
#     x=random.randrange(5,10)
#     print(x,end=' ')

# 5.0 --- 10.0 random 包括10
print('0.0 --- 5.0 random')
for i in range(0,10):
    x=random.randint(5,10)
    print(x,end=' ')