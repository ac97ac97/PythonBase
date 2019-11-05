import os.path
from datetime import datetime
f_name='text.txt'
af_name=r'F:\\Python_project\\py_for\\venv\\src\\ctrl_file\\text.txt'

basename=os.path.basename(af_name)
print(basename)

dirname=os.path.dirname(af_name)
print(dirname)

print(os.path.abspath(f_name))

print(os.path.getsize(f_name))

atime=datetime.fromtimestamp(os.path.getatime(f_name))
print(atime)

ctime=datetime.fromtimestamp(os.path.getctime(f_name))
print(ctime)

mtime=datetime.fromtimestamp(os.path.getmtime(f_name))
print(mtime)

print(os.path.isfile(dirname))
print(os.path.isdir(dirname))
print(os.path.isfile(f_name))
print(os.path.isdir(f_name))
print(os.path.exists(f_name))
