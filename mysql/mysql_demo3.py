#!/usr/bin/python3
# coding=UTF-8

#================================================================
#   Copyright (C) 2018 HALO Ltd. All rights reserved.
#   
#   文件名称：mysql_demo2.py
#   创 建 者：Zhangdunfeng
#   创建日期：2018-11-22 15:54:16
#   描    述：插入数据操作
#
#================================================================

import pymysql

db = pymysql.connect("192.168.88.128","root","root","zdf")

cursor = db.cursor()


sql = """INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME)
         VALUES('MAC','ZDF','22','M',2000)"""
try:
    cursor.execute(sql)
    db.commit()
    print("successful")
except:
    db.rollback()
    print("error")

db.close()

