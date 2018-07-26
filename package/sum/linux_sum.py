#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
@author: tanglei
@contact: tanglei_0315@163.com
@file: linux_sum.py
@time: 2018/5/23 17:37
'''
import os
import sys
import json
import shutil
import time
from salt import client
#在Linux系统上面运行导入模块需要将模块的路径加入到系统变量中才可以以
BASE_DIR = os.path.abspath(os.path.dirname(os.getcwd())+os.path.sep+"..")
sys.path.append(BASE_DIR)
from package.common.common import hostname,system,IsHashEqual,server_list,find_dir,alter

#全局变量
#new_data_path = os.path.abspath(os.path.dirname(os.getcwd()) + os.path.sep + ".." + os.path.sep + "data" + os.path.sep + "new")
#old_data_path = os.path.abspath(os.path.dirname(os.getcwd()) + os.path.sep + ".." + os.path.sep + "data" + os.path.sep + "old")
new_data_path = os.path.abspath(os.getcwd() + os.path.sep + "data" + os.path.sep + "new")
old_data_path = os.path.abspath(os.getcwd() + os.path.sep + "data" + os.path.sep + "old")

#通过saltstack获取服务器主机名的信息
def get_hostname(host):
    try:
        local = client.LocalClient()
        cmd = local.cmd(host,'grains.item',['nodename'])
        hostname_info = {"hostname":cmd[host]['nodename']}
        return hostname_info
    except Exception,e:
        print e

#通过saltstack获取cpu的信息
def get_cpuinfo(host):
    try:
        local = client.LocalClient()
        operating_system = system(host)
        if operating_system == 'linux':
            cmd = local.cmd(host,'grains.item',['cpu_module','cpu_physical','cpu_cores','cpu_processor'])
            cpu_info = {"cpu":cmd[host]}
            return cpu_info
        elif operating_system == 'windows':
            print 'windows'
        else:
            print 'other os'
    except Exception,e:
        print e

#将服务器信息汇总并存放在/data/new目录下面对应的主机名文件中
def data_sum():

    sum_data = {}

    for item in server_list():

        sum_data.update(get_hostname(item))
        sum_data.update(get_cpuinfo(item))
        sum_data.update({'modify':0})

        jsObj = json.dumps(sum_data)
        new_file = os.path.join(new_data_path, item)
        f = open(new_file, 'w')
        f.write(jsObj)
        f.close()

#将在old目录下面没有文件所对应的new目录下面的文件中的modify状态修改为1，以及通过md5对比文件不相等的情况下将modify状态修改为1
def modify_status(host):

    sum_data = {}

    sum_data.update(get_hostname(host))
    sum_data.update(get_cpuinfo(host))
    sum_data.update({'modify': 1})

    jsObj = json.dumps(sum_data)
    new_file = os.path.join(new_data_path, host)
    f = open(new_file, 'w')
    f.write(jsObj)
    f.close()

#如果old目录下面没有文件，则将new目录下面的文件拷贝到old目录下面，并将new目录下面的文件中的modify的值变为1
#如果old目录下面有文件，就和new目录下面的文件进行md5的比较是否一致，如果一致modify的值不变还为0，不一致则将nwe目录下面的文件中的modify的值变为1
def file_compare():

    for item in hostname(new_data_path):

        new_file = os.path.join(new_data_path, item)
        old_file = os.path.join(old_data_path, item)
        result = find_dir(old_file)
        print result

        if result == True:
            compare_result = IsHashEqual(new_file,old_file)
            print compare_result
            if compare_result == 'equality':
                pass
            else:
                modify_status(item)
        else:
            shutil.copy(new_file, old_file)
            modify_status(item)