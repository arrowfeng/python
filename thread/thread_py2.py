#!/usr/bin/python3
# coding=UTF-8

#================================================================
#   Copyright (C) 2018 HALO Ltd. All rights reserved.
#   
#   文件名称：thread_py2.py
#   创 建 者：Zhangdunfeng
#   创建日期：2018-11-23 09:05:23
#   描    述：_thread python2的线程处理模块，python3已废弃，不过可以兼容
#
#================================================================


import _thread
import time

def print_time(threadName, delay):
    count=0
    while count<5:
        time.sleep(delay)
        count+=1
        print("%s:%s" % ( threadName, time.ctime(time.time())))

try:
    _thread.start_new_thread( print_time, ("Thread-1",2, ))
    _thread.start_new_thread( print_time, ("Thread-2",4, ))
except:
    print("Error: 无法启动线程")

while 1:
    pass






