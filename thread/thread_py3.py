#!/usr/bin/python3
# coding=UTF-8

#================================================================
#   Copyright (C) 2018 HALO Ltd. All rights reserved.
#   
#   文件名称：thread_py3.py
#   创 建 者：Zhangdunfeng
#   创建日期：2018-11-23 09:14:48
#   描    述：threading模块 python3专属
#
#================================================================


import threading
import time

exitFlag=0

class myThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print("开始线程：" + self.name)
        print_time(self.name, self.counter, 5)
        print("退出线程：" + self.name)


def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            threadName.exit()#退出线程
        time.sleep(delay)
        print("%s: %s" % (threadName, time.ctime(time.time())))
        counter-=1

#创建线程
thread1=myThread(1,"Thread-1",1)
thread2=myThread(2,"Thread-2",2)

#开启线程
thread1.start()
thread2.start()

#join所完成的工作就是线程同步，即主线程任务结束之后，进入阻塞状态，一直等待其他的子线程执行结束之后，主线程才终止
thread1.join()
thread2.join()
print("退出主线程")



    



