#!/usr/bin/python3
# coding=UTF-8

#================================================================
#   Copyright (C) 2018 HALO Ltd. All rights reserved.
#   
#   文件名称：xml_dom.py
#   创 建 者：Zhangdunfeng
#   创建日期：2018-11-23 14:19:42
#   描    述：使用dom解析xml
#
#================================================================

from xml.dom.minidom import parse
import xml.dom.minidom

#使用minidom解析器打开XML文档
DOMTree=xml.dom.minidom.parse("movies.xml")
collection=DOMTree.documentElement
if collection.hasAttribute("shelf"):
    print("Root element: %s " % collection.getAttribute("shelf"))

#在集合中获取所有电影
movies=collection.getElementsByTagName("movie")

#打印每部电影的详细信息
for movie in movies:
    print("*****Movie*****")
    if movie.hasAttribute("title"):
        print("Title: %s" % movie.getAttribute("title"))
    
    type=movie.getElementsByTagName('type')[0]
    print("Type: %s" % type.childNodes[0].data)
    format=movie.getElementsByTagName('format')[0]
    print("Format: %s" % format.childNodes[0].data)
    rating=movie.getElementsByTagName('rating')[0]
    print("Rating: %s" % rating.childNodes[0].data)
    stars=movie.getElementsByTagName('stars')[0]
    print("Stars: %s" % stars.childNodes[0].data)
    description=movie.getElementsByTagName('description')[0]
    print("Description: %s" % description.childNodes[0].data)




