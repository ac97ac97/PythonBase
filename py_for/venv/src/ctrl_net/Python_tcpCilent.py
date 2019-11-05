import socket

#简单的聊天工具--客户端

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#连接服务器
s.connect(('127.0.0.1',8888))  #设置自己的服务器名称或者IP地址


#给服务器发送数据
s.send(b'Hello')

#从服务器接收数据
data=s.recv(1024)
print('从服务器接收的数据为:{0}'.format(data.decode()))

#释放资源 二者都是socket对象
s.close()