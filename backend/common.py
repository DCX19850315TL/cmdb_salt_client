#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
@author: tanglei
@contact: tanglei_0315@163.com
@file: common.py
@time: 2018/3/21 18:05
'''
#定义字符串转换数字的公共函数
def convert_to_int(value,default=0):
    try:
        result = int(value)
    except Exception,e:
        result = default
    return result

#定义单位为mb的转换为gb的公共函数
def convert_mb_to_gb(value,default=0):
    try:
        value = value.strip('MB')
        result = round(int(value)/1024,ndigits=2)
    except Exception,e:
        result = result
    return result

#print type(convert_to_int('123'))
#print convert_mb_to_gb('211MB')
