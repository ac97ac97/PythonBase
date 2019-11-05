# import threading
# import time
# #等待线程结束
# # 共享变量
# value=0
# #线程体函数
# def thread_body():
#     global value
#     #当前线程对象
#     print('ThreadA 开始...')
#     for n in range(2):
#         print('ThreadA 执行...')
#         value +=1
#         #线程休眠
#         time.sleep(1)
#     print('ThreadA 结束...')
#
# #主函数
#
# def main():
#     print('主线程开始...')
#     #创建线程对象t1
#     t1=threading.Thread(target=thread_body,name='ThreadA')
#     #启动线程t1
#     t1.start()
#     #主线程被阻塞等待t1线程结束
#     # t1.join()
#     print('value={0}'.format(value))
#     print('主线程结束...')
# if __name__=='__main__':
#     main()



#线程停止

import threading
import time

# 线程停止变量
isrunning = True


# 线程体函数
def thread_body():
    while isrunning:
        #线程开始工作
        print('下载中...')
        #线程休眠
        time.sleep(5)
        print('执行完成!')



# 主函数

def main():
    # 创建线程对象t1
    t1 = threading.Thread(target=thread_body)
    # 启动线程t1
    t1.start()
    #从键盘上输入停止指令exit
    command=input('请输入停止指令：')
    if command == 'exit':
        global isrunning
        isrunning=False

if __name__ == '__main__':
    main()

