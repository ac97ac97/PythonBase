import socket

#文件上传工具 ---客户端

HOST = '127.0.0.1'
POST=8888
f_name='F:\\Python_project\\py_for\\venv\src\\ctrl_net\\test_copy.txt'

#服务器地址
server_address=(HOST,POST)

with socket.socket(socket.AF_INET,socket.SOCK_DGRAM) as s:
    with open(f_name,'r') as f:
        while True:
            data=f.read(1024)
            if data:
                #发送数据
                s.sendto(data.encode(),server_address)
            else:
                #发送结束标志
                s.sendto(b'bye',server_address)
                #文件中没有可读取的数据则退出
                break

    print('客户端上传数据完成')
