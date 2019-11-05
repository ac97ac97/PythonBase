import socket

#文件上传工具 ---客户端

HOST = '127.0.0.1'
POST=8888

f_name='F:\\Python_project\\py_for\\venv\\src\\ctrl_net\\black_white.jpg'

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.connect((HOST,POST))
    with open(f_name,'rb') as f:
        b=f.read()
        s.sendall(b)

    print('客户端上传数据完成')
