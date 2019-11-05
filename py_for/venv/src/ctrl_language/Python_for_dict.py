student_dict = {102:'zhangsan',105:'lisi',109:'wangwu'}
print('------遍历见----')
for student_id in student_dict.keys():
    print('学号 ： '+str(student_id))
print("----------------")
for student_name in student_dict.values():
    print("学生 ：" +student_name)
print("----------------")
for student_id,student_name in student_dict.items():
    print("学号： {0}--学生: {1}".format(student_id,student_name))