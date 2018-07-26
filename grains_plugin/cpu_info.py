#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
@author: tanglei
@contact: tanglei_0315@163.com
@file: cpu_info.py
@time: 18-4-25 下午3:23
'''
import os
import commands

def cpuinfo():

    cpu_sum_info = {}

    raw_data = {
        'cpu_module':"cat /proc/cpuinfo | grep 'model name' | head -1",
        'cpu_physical':"cat /proc/cpuinfo | grep 'physical id' | sort | uniq | wc -l",
        'cpu_cores':"cat /proc/cpuinfo | grep 'cores' | sort | uniq | awk '{print $4}'",
        'cpu_processor':"cat /proc/cpuinfo | grep 'processor' | wc -l",
    }

    for k,v in raw_data.items():
        try:
            cmd = commands.getoutput(v)
            raw_data[k]=cmd.strip()
            #print(raw_data['cpu_module'])
        except Exception,e:
            print(e)

    data = {
        'cpu_physical':raw_data['cpu_physical'],
        'cpu_cores':raw_data['cpu_cores'],
        'cpu_processor':raw_data['cpu_processor']
    }

    cpu_module = raw_data['cpu_module'].split(':')
    if (cpu_module) > 1:
        data['cpu_module'] = cpu_module[1].strip()
    else:
        data['cpu_module'] = -1

    cpu_status = {'modify': 1}
    cpu_data = {'data': data}
    cpu_sum_info.update(cpu_status)
    cpu_sum_info.update(cpu_data)

    # print cpu_sum_info
    return cpu_sum_info