#!/anaconda3/bin/python
# coding=UTF-8

#================================================================
#   Copyright (C) 2018 HALO Ltd. All rights reserved.
#   
#   文件名称：pickle_demo1.py
#   创 建 者：Zhangdunfeng
#   创建日期：2018-11-20 17:01:20
#   描    述：使用pickle模块将数据对象保存到文件
#
#================================================================


import pickle

data1 = {'a': [1, 2.0, 3, 4+6j],
         'b': ('string',u'Unicode string'),
         'c': None}

selfref_list = [1, 2, 3]
selfref_list.append(selfref_list)

output = open('data.pkl', 'wb')

pickle.dump(data1, output)

pickle.dump(selfref_list, output, -1)

output.close()
