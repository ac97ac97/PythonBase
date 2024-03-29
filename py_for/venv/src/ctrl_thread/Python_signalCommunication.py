#使用condition实现线程之间的通信
# import threading
# import time
# import random
#
# #创建条件变量对象
# condition=threading.Condition()
#
# class Stack:
#     def __init__(self):
#         #堆栈指针初始值为0
#         self.pointer=0
#         #堆栈有5个数字空间
#         self.data=[-1,-1,-1,-1,-1]
#     #压栈方法
#     def push(self,c):
#         global condition
#         condition.acquire()
#         #堆栈已满不能压栈
#         while self.pointer == len(self.data):
#             #等待其他线程把数据出栈
#             condition.wait()
#         #通知其他线程把数据出栈
#         condition.notify()
#         #数据压栈
#         self.data[self.pointer] = c
#         #指针向上移动
#         self.pointer +=1
#         condition.release()
#
#     # 出栈方法
#     def pop(self):
#         global condition
#         condition.acquire()
#         #堆栈无数据不能出栈
#         while self.pointer == 0:
#             #等待其他线程把数据压栈
#             condition.wait()
#         #通知其他线程压栈
#         condition.notify()
#         # 指针向下移动
#         self.pointer -= 1
#
#         data=self.data[self.pointer]
#         condition.release()
#         #数据出栈
#         return data
#
#
# #创建堆栈stack对象
# stack = Stack()
#
# #生产者线程体函数
# def producer_thread_body():
#     global stack #声明为全局变量
#     #生产10个数字
#     for i in range(10):
#         #把数字压栈
#         stack.push(i)
        #打印数字
        # print('生产：{0}'.format(i))
        # #每产生一个数字线程就睡眠
        # time.sleep(1)

#消费者线程体函数
#
# def customer_thread_body():
#     global stack  # 声明为全局变量
#     #从堆栈中读取数字
#     for i in range(10):
#          # 从堆栈中读取数字
#          x=stack.pop()
#          #打印数字
#          print('消费：{0}'.format(x))
#          # 每消费一个数字线程就睡眠
#          time.sleep(1)
#
# # 主函数
#
# def main():
#     # 创建生产者对象 producer
#     producer = threading.Thread(target=producer_thread_body)
#     # 启动生产者线程
#     producer.start()
#     # 创建消费者对象 customer
#     customer = threading.Thread(target=customer_thread_body)
#     # 启动消费者线程
#     customer.start()
#
# if __name__ == '__main__':
#     main()


#使用Event实现线程之间的通信

import threading
import time
import random

event=threading.Event()
class Stack():
    def __init__(self):
        #堆栈指针初始值为0
        self.pointer=0
        #堆栈有5个数字空间
        self.data=[-1,-1,-1,-1,-1]

    #压栈方法
    def push(self,c):
        global event
        #堆栈已满不能压栈
        while self.pointer == len(self.data):
            #等待其他线程把数据出栈
            event.wait()
        #通知其他线程把数据出栈
        event.set()
        #数据压栈
        self.data[self.pointer] = c
        #指针向上移动
        self.pointer +=1

    # 出栈方法
    def pop(self):
        global event
        #堆栈无数据不能出栈
        while self.pointer == 0:
            #等待其他线程把数据压栈
            event.wait()
        #通知其他线程压栈
        event.set()
        # 指针向下移动
        self.pointer -= 1

        data=self.data[self.pointer]
        #数据出栈
        return data


#创建堆栈stack对象
stack = Stack()

#生产者线程体函数
def producer_thread_body():
    global stack #声明为全局变量
    #生产10个数字
    for i in range(10):
        #把数字压栈
        stack.push(i)
        #打印数字
        print('生产：{0}'.format(i))
        #每产生一个数字线程就睡眠
        time.sleep(1)

#消费者线程体函数

def customer_thread_body():
    global stack  # 声明为全局变量
    #从堆栈中读取数字
    for i in range(10):
         # 从堆栈中读取数字
         x=stack.pop()
         #打印数字
         print('消费：{0}'.format(x))
         # 每消费一个数字线程就睡眠
         time.sleep(1)

# 主函数

def main():
    # 创建生产者对象 producer
    producer = threading.Thread(target=producer_thread_body)
    # 启动生产者线程
    producer.start()
    # 创建消费者对象 customer
    customer = threading.Thread(target=customer_thread_body)
    # 启动消费者线程
    customer.start()

if __name__ == '__main__':
    main()
