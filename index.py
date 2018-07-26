#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
@author: tanglei
@contact: tanglei_0315@163.com
@file: index.py
@time: 18-4-25 下午3:21
'''
import os
import httplib
import urllib
import time
import json
import logging
from package.sum import linux_sum
from package.common import common

#全局变量
#new_data_path = os.path.abspath(os.path.dirname(os.getcwd()) + os.path.sep + ".." + os.path.sep + "data" + os.path.sep + "new")
#old_data_path = os.path.abspath(os.path.dirname(os.getcwd()) + os.path.sep + ".." + os.path.sep + "data" + os.path.sep + "old")
new_data_path = os.path.abspath(os.getcwd() + os.path.sep + "data" + os.path.sep + "new")
old_data_path = os.path.abspath(os.getcwd() + os.path.sep + "data" + os.path.sep + "old")

def RequestUrl(host,port,source,params,timeout):

    headers = {"Content-type":"application/x-www-form-urlencoded"}

    try:
        conn = httplib.HTTPConnection(host,port,timeout)
        conn.request('POST',source,params,headers)
        response = conn.getresponse()
        original = response.read()
        print original
    except Exception,e:
        print e

linux_sum.data_sum()
linux_sum.file_compare()
'''
for item in common.hostname(new_data_path):
    file_path = os.path.join(new_data_path,item)
    f = open(file_path,'r')
    server_info = f.readline()
    print server_info
'''
'''
cpu = cpuinf

server_info = {
   'cpu':cpu
}

logger = logging.getLogger('test')
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s' )
filehandler = logging.handlers.T
'''

if __name__ == '__main__':
    try:
        for item in common.hostname(new_data_path):
            file_path = os.path.join(new_data_path,item)
            f = open(file_path,'r')
            server_info = f.readline()
            print server_info
            #RequestData = {'data':server_info}
            RequestData = urllib.urlencode({'data':json.dumps(server_info)})
            result = RequestUrl('10.160.92.61','9000','/api/receive_server_info/',RequestData,30)
    except Exception,e:
        print e