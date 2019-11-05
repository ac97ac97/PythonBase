import socket

#简单的聊天工具--服务端

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('',8888))
print('服务器启动...')

#从客户端接收数据(“指定的字符集”) 默认编码格式是utf-8
data,client_address = s.recvfrom(1024)
print('从客服端接收的消息 ： {0}'.format(data.decode()))  #decode返回1指定的字符集默认编码格式是utf-8

#给客户端发送消息
s.sendto('你好'.encode(),client_address)  #encode返回1指定的字符集默认编码格式是utf-8

#释放资源 二者都是socket对象
s.close()
