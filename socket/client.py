#!/usr/bin/python3
# coding=UTF-8

#================================================================
#   Copyright (C) 2018 HALO Ltd. All rights reserved.
#   
#   文件名称：client.py
#   创 建 者：Zhangdunfeng
#   创建日期：2018-11-22 16:38:30
#   描    述：socket练习 client
#
#================================================================

import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()

port = 9999

s.connect(('192.168.88.128',port))

msg = s.recv(1024)

s.close()

print(msg.decode('utf-8'))




