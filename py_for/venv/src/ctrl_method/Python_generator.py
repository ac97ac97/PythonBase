def square(num):
     # n_list=[]
    # for i in range(1,num+1):
    #     n_list.append(i*i)
    # return n_list
    # for i in square(5):
    #     print(i , end=' ')
    for i in range(1,num+1):
        yield i*i
for i in square(5):
        print(i,end=' ')