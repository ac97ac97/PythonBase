#os模块
import os
f_name='F:\\Python_project\\py_for\\venv\src\\ctrl_file\\text.txt'
copy_f_name = 'F:\\Python_project\\py_for\\venv\\src\\ctrl_file\\copy.txt'
with open(f_name,'r') as f:
    b=f.read()
    with open(copy_f_name,'w') as copy_f:
        copy_f.writelines(b)
        print('----------------------------------------------------------------')
    try:
        os.rename(copy_f_name,'F:\\Python_project\\py_for\\venv\\src\\ctrl_file\\copy2.txt')
    except OSError:
        os.remove('F:\\Python_project\\py_for\\venv\\src\\ctrl_file\\copy2.txt')
    print(os.listdir(os.curdir))
    print(os.listdir(os.pardir))
    try:
        os.mkdir('F:\\Python_project\\py_for\\venv\\src\\ctrl_file\\subdir')
        print('----------------------------------------------------------------')
    except:
        os.rmdir('F:\\Python_project\\py_for\\venv\\src\\ctrl_file\\subdir')
    for item in os.walk('.'):
        print(item)