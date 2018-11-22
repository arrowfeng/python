#!/usr/bin/python3
# coding=UTF-8

#================================================================
#   Copyright (C) 2018 HALO Ltd. All rights reserved.
#   
#   文件名称：mysql_demo1.py
#   创 建 者：Zhangdunfeng
#   创建日期：2018-11-22 15:47:51
#   描    述：MySQL 连接练习 查看数据库版本
#
#================================================================

import pymysql

db = pymysql.connect("192.168.88.128","root","root","zdf")

cursor = db.cursor()

cursor.execute("SELECT VERSION()")

data = cursor.fetchone()

print("Database version:{0}".format(data))

db.close()
