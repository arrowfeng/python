#!/usr/bin/python3
# coding=UTF-8

#================================================================
#   Copyright (C) 2018 HALO Ltd. All rights reserved.
#   
#   文件名称：json_demo.py
#   创 建 者：Zhangdunfeng
#   创建日期：2018-11-23 14:41:50
#   描    述：解析Json
#
#================================================================


import json

data1 = {
    'no':1,
    'name':'HALO',
    'url':'http://halo.cn'
}

#将字典对象变成json数据格式
json_str=json.dumps(data1)
print("Python原始数据：", repr(data1))
print("JSON对象：", json_str)

with open('data.json','w') as f:
    json.dump(json_str,f)


#将JSON对象转换为字典
data2=""
with open('data.json','r') as f:
    data2=json.loads(json.load(f))#python从文件读取.json文件是获得字符串，还需转换成python对象
print("data['name']:",data2['name'])
print("data['url']:",data2['url'])







