#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
@author: tanglei
@contact: tanglei_0315@163.com
@file: index2.py.py
@time: 2018/3/27 17:14
'''
import httplib
import urllib
import time
import json
from plugins import PluginApi

class Program():
    def __init__(self):
        self.server_response = PluginApi.get_server_info()

    def execute(self):
        if self.server_response.status:

            params = urllib.urlencode({"data":json.dumps(self.server_response.data)})
            self.submit_data('127.0.0.1','9000','/receive_server_info/',params,30)

    def submit_data(self,host,port,source,params,timeout):
        headers = {"Content-type":"application/json"}
        try:
            conn = httplib.HTTPConnection(host,port,timeout)
            conn.request('POST',source,params,headers)
            response = conn.getresponse()
            original = response.read()
        except Exception,e:
            raise e
        return original

if __name__ == '__main__':
    times = 0
    while True:
        objProgram = Program()
        objProgram.execute()
        times += 1
        time.sleep(10)
