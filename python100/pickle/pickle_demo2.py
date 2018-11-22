#!/anaconda3/bin/python
# coding=UTF-8

#================================================================
#   Copyright (C) 2018 HALO Ltd. All rights reserved.
#   
#   文件名称：pickle_demo2.py
#   创 建 者：Zhangdunfeng
#   创建日期：2018-11-20 17:15:00
#   描    述：使用pickle模块从文件中重构python对象
#
#================================================================

import pprint, pickle

pkl_file = open('data.pkl', 'rb')

data1 = pickle.load(pkl_file)
pprint.pprint(data1)

data2 = pickle.load(pkl_file)
pprint.pprint(data2)

pkl_file.close()
