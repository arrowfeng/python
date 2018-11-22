#!/usr/bin/python3
# coding=UTF-8

#================================================================
#   Copyright (C) 2018 HALO Ltd. All rights reserved.
#   
#   文件名称：server.py
#   创 建 者：Zhangdunfeng
#   创建日期：2018-11-22 16:27:00
#   描    述：socket编程练习 服务端
#
#================================================================

import socket
import sys

serversocket = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM
        )

host = socket.gethostname()

port = 9999

#绑定主机和端口
serversocket.bind((host,port))

#设置最大连接数
serversocket.listen(5)

while True:
    #建立客户端连接
    clientsocket, addr = serversocket.accept()

    print("连接地址：%s" % str(addr))

    msg='欢迎访问Halo！' + "\r\n"
    clientsocket.send(msg.encode('utf-8'))
    clientsocket.close()



