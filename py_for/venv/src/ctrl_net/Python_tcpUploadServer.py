import socket

#文件上传工具 ---服务端

HOST = ''
POST=8888

f_name='F:\\Python_project\\py_for\\venv\\src\\ctrl_net\\black_white.jpg'

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as conn:
    #创建字节序列对象列表 作为接收数据的缓冲区
    buffer = []
    while True:   #反复接收数据
        data= conn.recv(1024)
        if data:
            #接收的数据加入缓冲区
            buffer.append(data)
        else:
            #没有接收到数据则退出
            break
    #将接收的字节序列对象列表合并为一字序列对象
    b=bytes().join(buffer)
    with open(f_name,'wb') as f:
        f.write(b)
    print('服务器接收完毕')
