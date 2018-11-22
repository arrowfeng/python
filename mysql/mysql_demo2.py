#!/usr/bin/python3
# coding=UTF-8

#================================================================
#   Copyright (C) 2018 HALO Ltd. All rights reserved.
#   
#   文件名称：mysql_demo2.py
#   创 建 者：Zhangdunfeng
#   创建日期：2018-11-22 15:54:16
#   描    述：创建数据库表
#
#================================================================

import pymysql

db = pymysql.connect("192.168.88.128","root","root","zdf")

cursor = db.cursor()

cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

sql = """CREATE TABLE EMPLOYEE(
         FIRST_NAME CHAR(20) NOT NULL,
         LAST_NAME CHAR(20),
         AGE INT,
         SEX CHAR(1),
         INCOME FLOAT)"""

cursor.execute(sql)

db.close()

