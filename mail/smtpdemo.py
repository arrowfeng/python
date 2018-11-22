#!/usr/bin/python3
# coding=UTF-8

#================================================================
#   Copyright (C) 2018 HALO Ltd. All rights reserved.
#   
#   文件名称：smtpdemo.py
#   创 建 者：Zhangdunfeng
#   创建日期：2018-11-22 17:02:14
#   描    述：发送邮件测试
#
#================================================================

import smtplib
from email.mime.text import MIMEText
from email.header import Header

#第三方SMTP服务
mail_host="smtp.163.com"
mail_user="18213552822@163.com"
mail_pass="halozdf123"

sender='18213552822@163.com'
receivers=['halo@hust.edu.cn']

message=MIMEText('Python邮件发送测试。。。','plain','utf-8')
message['From']=Header("HALO教程","utf-8")
message['To']=Header("测试","utf-8")

subject='Python SMTP 邮件测试'
message['Subject']=Header(subject,"utf-8")

try:
    smtpObj=smtplib.SMTP()
    smtpObj.connect(mail_host,25)
    smtpObj.login(mail_user,mail_pass)
    smtpObj.sendmail(sender,receivers,message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException as e:
    print(e)
    print("Error:无法发送邮件")


