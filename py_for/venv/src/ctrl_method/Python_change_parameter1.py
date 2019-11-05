def show_info(step=':',**info):
    print('--------------------')
    for key,value in info.items():
        print('{0} {2} {1}'.format(key,value,step))
show_info('->',name='Tony',age=18,sex=True)
show_info(student_name='Tony',student_no='1000',step='-')
stu_dict = {'name':'Tony','age':18}
show_info(**stu_dict,sex=True,step='=')