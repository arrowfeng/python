#!/usr/bin/python
# coding=UTF-8

#================================================================
#   Copyright (C) 2018 HALO Ltd. All rights reserved.
#   
#   文件名称：thread_unlock.py
#   创 建 者：Zhangdunfeng
#   创建日期：2018-11-23 09:30:34
#   描    述：threading 数据共享问题。一个列表里所有元素都是0，线程"set"从后向前把所有元素改成1，而线程"print"负责从前往后读取列表并打印。 那么，可能线程"set"开始改的时候，线程"print"便来打印列表了，输出就成了一半0一半1，这就是数据的不同步。
#
#================================================================

import threading

class setThread(threading.Thread):
    
    def __init__(self, threadID, name, data):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.data = data
    
    def run(self):
        print("开启设置线程：" + self.name)
        for i in reversed(range(len(data))):
            self.data[i]=1
        print("线程结束：" + self.name)


#打印线程
class printThread(threading.Thread):
    
    def __init__(self, threadID, name, data):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.data = data
    
    def run(self):
        print("开启设置线程：" + self.name)
        print(self.data)
        print("线程结束：" + self.name)

data=[0,0,0,0,0,0,0,0,0,0,0]
pthread=printThread(1,'print', data)
sthread=setThread(2,'set', data)


pthread.start()
sthread.start()

pthread.join()
sthread.join()


print("主线程完毕")




















