#打开文件

f=open('text.txt','w+')
f.write('World')

f=open('text.txt','r+')
f.write('Hello')

f=open('text.txt','a')
f.write(' ')

fname=r'F:\Python_project\py_for\venv\src\ctrl_file\text.txt'
f=open(fname,'a+')
f.write('World')

