#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
@author: tanglei
@contact: tanglei_0315@163.com
@file: index.py
@time: 2018/3/21 17:32
'''
import httplib
import urllib
import time
import json

def RequestUrl(host,port,source,params,timeout):
    headers = {"Content-type":"application/x-www-form-urlencoded"}

    try:
        conn = httplib.HTTPConnection(host,port,timeout)
        conn.request('POST',source,params,headers)
        response = conn.getresponse()
        original = response.read()
        print original
    except Exception,e:
        raise e
    return original

server_info = {
    'a':'aa'
}

if __name__ == '__main__':
    #times = 0
    #while True:
        #RequestData = {'data':server_info}
        #RequestData = json.dumps(RequestData)
        RequestData = urllib.urlencode({'data':server_info})
        result = RequestUrl('127.0.0.1','9000','/receive_server_info/',RequestData,30)
        print '======第%d次请求，结果为: %s========= %(times,result)'
        #times += 1
        #time.sleep(3)