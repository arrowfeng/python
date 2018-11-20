#!/anaconda3/bin/python3
# coding=UTF-8

#================================================================
#   Copyright (C) 2018 HALO Ltd. All rights reserved.
#   
#   文件名称：demo1.py
#   创 建 者：Zhangdunfeng
#   创建日期：2018-11-19 23:52:16
#   描    述：Fibonacci series
#
#================================================================

n=10
a,b=0,1
while b < n:
    print(b,end=',')
    a,b=b,a+b
