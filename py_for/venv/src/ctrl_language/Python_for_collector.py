# student_set = {"张三","李四","找六"}
# for item in student_set:
#     print(item)
# for i,item in enumerate(student_set):
#     print("{0}----{1}".format(i,item))
input_list=[1,23,3,4,4,2,3,7,8]
n_list = [x ** 2  for x in input_list]
print(n_list)
n_set = {x ** 2 for x in input_list }
print(n_set)