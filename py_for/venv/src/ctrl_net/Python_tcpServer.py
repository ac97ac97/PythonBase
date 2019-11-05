import socket

#简单的聊天工具--服务端

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('',8888))
s.listen()
print('服务器启动...')

#等待客户端连接
conn,address = s.accept()
#客户端连接成功
print(address)

#从客户端接收数据(“指定的字符集”) 默认编码格式是utf-8
data = s.recv()
print('从客服端接收的消息 ： {0}'.format(data.decode()))  #decode返回1指定的字符集默认编码格式是utf-8

#给客户端发送消息
conn.send('你好'.encode())  #encode返回1指定的字符集默认编码格式是utf-8

#释放资源 二者都是socket对象
conn.close()
s.close()
