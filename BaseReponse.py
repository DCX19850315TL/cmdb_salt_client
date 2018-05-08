#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
@author: tanglei
@contact: tanglei_0315@163.com
@file: BaseReponse.py
@time: 2018/3/29 17:11
'''
from backend import bll

def main():
    result = bll.get_computername()

    if result.status:
        print 'data',result.data
    else:
        print 'error',result.error

if __name__ == '__main__':
    main()
