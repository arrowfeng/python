#!/usr/bin/python
# coding=UTF-8

#================================================================
#   Copyright (C) 2018 HALO Ltd. All rights reserved.
#   
#   文件名称：practice_day1.py
#   创 建 者：Zhangdunfeng
#   创建日期：2018-11-19 23:38:08
#   描    述：给定一个数字范围，这些数字能组成多少个互不相同且无重复的三位数。
#
#================================================================
start=1
end=5
for i in range(start,end):
    for j in range(start,end):
        for k in range(start,end):
            if (k != i) and (k != j) and (j != i):
                print (i,j,k)

