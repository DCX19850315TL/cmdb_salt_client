#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
@author: tanglei
@contact: tanglei_0315@163.com
@file: PluginApi.py
@time: 2018/3/29 17:52
'''
import os
from backend.response import BaseResponse
from plugins.MemoryPlugin import MemoryPlugin

def get_server_info():
    response = BaseResponse()
    try:
        server_info = {}
        server_info['hostname'] = os.environ['HOSTNAME']

        memObj = MemoryPlugin()
    except Exception,e:
        response.message = e.message

    return response

