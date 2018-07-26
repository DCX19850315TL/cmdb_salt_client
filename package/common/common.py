#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
@author: tanglei
@contact: tanglei_0315@163.com
@file: common.py
@time: 2018/5/11 17:07
'''
import os
import commands
import hashlib
from salt.client import LocalClient

#获取salt接受认证的主机名列表，以方便按照主机名获取数据。
def hostname(file_dir):

    for root,dirs,files in os.walk(file_dir):
        root=root
        dirs=dirs
        files=files
        return files

#查看服务器是linux系统还是windows系统
def system(hostname):
    try:
        local = LocalClient()
        sys = local.cmd(hostname,'grains.item',['kernel'])
        if sys[hostname]['kernel'] == 'Linux':
            return 'linux'
        elif sys[hostname]['kernel'] == 'Windows':
            return 'windows'
    except Exception,e:
        print e

#将linux系统或者windows系统的服务器列表返回
def server_list():
    try:
        linux_k_list=[]
        local = LocalClient()
        for item in hostname('/etc/salt/pki/master/minions'):
            sys = local.cmd(item, 'grains.item', ['kernel'])
            if sys[item]['kernel'] == 'Linux':
                for k,v in sys.items():
                    linux_k = unicode.encode(k)
                    #os_list_path = os.path.abspath(os.path.dirname(os.getcwd()) + os.path.sep + ".." + os.path.sep + "data")
                    os_list_path = os.path.abspath(os.getcwd() + os.path.sep + "data")
                    os_list_file_linux = os.path.join(os_list_path,"linux_list.txt")
                    f = open(os_list_file_linux,'a')
                    f.write("|")
                    f.write(linux_k)
                    f.close()
            elif sys[item]['kernel'] == 'Windows':
                pass
            else:
                print 'other os'
    except Exception,e:
        print e

    try:
        f = open(os_list_file_linux, 'r')
        linux_str = f.read()
        linux_str_1 = linux_str[1:]
        linux_list = linux_str_1.split('|')
        f.close()
        f = open(os_list_file_linux, 'w')
        f.truncate()
        f.close()
        return linux_list
    except Exception,e:
        print e

#判断新旧服务器数据文件是否一致
def getHash(file_f):
    f = open(file_f,'r')
    line = f.readline()
    hash = hashlib.md5()
    while(line):
        hash.update(line)
        line = f.readline()
    return hash.hexdigest()
def IsHashEqual(f1,f2):
    str1=getHash(f1)
    str2=getHash(f2)
    if str1 == str2:
        return "equality"
    else:
        return "inequality"

#查找路径下的文件置否存在
def find_dir(old_file):

    if os.path.exists(old_file):
        return True
    else:
        return old_file

#将文件内容进行更换
def alter(file,old_str,new_str):

    file_data = ""
    with open(file,"r") as f:
        for line in f:
            if old_str in line:
                line = line.replace(old_str,new_str)
            file_data += line
    with open(file,"w") as f:
        f.write(file_data)