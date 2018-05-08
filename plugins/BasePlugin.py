#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
@author: tanglei
@contact: tanglei_0315@163.com
@file: BasePlugin.py
@time: 2018/3/21 17:54
'''
import platform

class BasePlugin(object):

    def execute(self):
        result = platform.system()
        if result == 'linux':
            return self.linux()
        elif result == 'windows':
            return self.windows()
        else:
            raise Exception('unknow os')

    def linux(self):
