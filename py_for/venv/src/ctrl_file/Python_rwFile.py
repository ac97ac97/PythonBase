#文本文件的读写
# f_name='F:\\Python_project\\py_for\\venv\src\\ctrl_file\\text.txt'
# with open(f_name,'r',encoding='utf-8') as f:
#     lines=f.readlines()
#     print(lines)
#     copy_f_name='F:\\Python_project\\py_for\\venv\\src\\ctrl_file\\copy.txt'
#     with open(copy_f_name,'w',encoding='utf-8') as copy_f:
#         copy_f.writelines(lines)
#         print('文件复制成功')

#二进制文件的读写

f_name='F:\\Python_project\\py_for\\venv\\src\\ctrl_file\\black_white.jpg'
with open(f_name,'rb') as f:
    b=f.read()
    copy_f_name='F:\\Python_project\\py_for\\venv\\src\\ctrl_file\\copy_black_white.jpg'
    with open(copy_f_name,'wb') as copy_f:
        copy_f.write(b)
        print('文件复制成功')