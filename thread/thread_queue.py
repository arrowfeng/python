#!/usr/bin/python3
# coding=UTF-8

#================================================================
#   Copyright (C) 2018 HALO Ltd. All rights reserved.
#   
#   文件名称：thread_queue.py
#   创 建 者：Zhangdunfeng
#   创建日期：2018-11-23 10:49:11
#   描    述：多线程使用优先级队列
#
#================================================================

import queue
import threading
import time

exitFlag=0

class myThread(threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID=threadID
        self.name=name
        self.q=q

    def run(self):
        print("开启线程：" + self.name)
        process_data(self.name, self.q)
        print("退出线程：" + self.name)

def process_data(threadName, q):
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            data=q.get()
            print("%s processing %s" % (threadName, data))
        queueLock.release()
        time.sleep(1)

threadList=["Thread-1", "Thread-2", "Thread-3"]
nameList=["One", "Two", "Three", "Four", "Five"]
queueLock=threading.Lock()
workQueue=queue.Queue(10)
threads=[]
threadID=1

for tName in threadList:
    thread=myThread(threadID, tName, workQueue)
    thread.start()
    threads.append(thread)
    threadID+=1

queueLock.acquire()
for word in nameList:
    workQueue.put(word)
queueLock.release()

while not workQueue.empty():
    pass

#通知线程退出
exitFlag=1

for t in threads:
    t.join()

print("退出主线程")















    






