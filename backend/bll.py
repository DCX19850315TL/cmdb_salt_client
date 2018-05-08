#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
@author: tanglei
@contact: tanglei_0315@163.com
@file: bll.py
@time: 2018/3/29 17:14
'''
import os
from backend.response import BaseResponse

def get_computername():
    response = BaseResponse()
    try:
        name = os.environ['COMPUTERNAME']
        response.data = name
        response.status = True
    except Exception,e:
        response.error = e.message
    return response