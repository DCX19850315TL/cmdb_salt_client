#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
@author: tanglei
@contact: tanglei_0315@163.com
@file: response.py
@time: 2018/3/29 17:15
'''
class BaseResponse():

    def __init__(self):
        self.status = False
        self.data = None
        self.error = ''