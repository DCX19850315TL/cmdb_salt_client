#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
@author: tanglei
@contact: tanglei_0315@163.com
@file: test.py
@time: 2018/5/23 17:37
'''
import os
import hashlib
'''
import os
new_data = os.path.abspath(os.path.dirname(os.getcwd())+os.path.sep+"data"+os.path.sep+"new")
a = os.path.abspath(os.path.dirname(os.getcwd())+os.path.sep+".."+os.path.sep+"data"+os.path.sep+"new")
print new_data
print a
'''

#判断新旧服务器数据文件是否一致
def compare(new_file,old_file):

    new_hash_file = hashlib.md5()
    old_hash_file = hashlib.md5()
    new_hash_file.update(new_file)
    old_hash_file.update(old_file)
    new_md5 = new_hash_file.hexdigest()
    old_md5 = old_hash_file.hexdigest()

    if new_md5 == old_md5:
        print "相等"
    else:
        print "不相等"

compare('1','1')

new_data = os.path.abspath(os.path.dirname(os.getcwd())+os.path.sep+".."+os.path.sep+"data"+os.path.sep+"new")
                new_file = os.path.join(new_data,item)
                jsObj = json.dumps(cpu_info)
                f = open(new_file,'a')
                f.write(jsObj)
                f.close()
                print cmd
                print type(cmd)
new_data = os.path.abspath(os.path.dirname(os.getcwd()) + os.path.sep + ".." + os.path.sep + "data" + os.path.sep + "new")
                new_file = os.path.join(new_data, item)
                f = file(new_file,'w')
                f.write('def')
                f.close()

def get_hostname():
    try:
        local = client.LocalClient()
        for item in hostname('/etc/salt/pki/master/minions'):
            cmd = local.cmd(item,'grains.item',['nodename'])
            hostname_info = {"hostname":cmd[item]}
            return hostname_info
    except Exception,e:
        print e

'''
def data_sum():

    sum_data = {}

    for item in server_list():

        sum_data.update(get_hostname(item))
        sum_data.update(get_cpuinfo(item))
        #sum_data.update(x)

        new_file = os.path.join(new_data_path, item)
        jsObj = json.dumps(sum_data)
        f = open(new_file, 'w')
        f.write(jsObj)
        f.close()
'''

'''
def file_compare():

    old_file_default = os.path.join(old_data_path, 'test')

    if os.path.exists(old_file_default):
        #os.remove(old_file_default)
        pass
    else:
        os.mknod(old_file_default)

    for item in hostname(new_data_path):

        result = find_dir(old_data_path,item)
        print result

        if result == 'null':
            print '没有文件'
            new_file = os.path.join(new_data_path, item)
            old_file = os.path.join(old_data_path, item)
            shutil.copy(new_file,old_file)
            #data_sum(modify=1)
        else:
            print '文件已经存在'
'''

'''
def compare(new_file,old_file):

    new_hash_file = hashlib.md5()
    old_hash_file = hashlib.md5()
    new_hash_file.update(new_file)
    old_hash_file.update(old_file)
    new_md5 = new_hash_file.hexdigest()
    old_md5 = old_hash_file.hexdigest()

    if new_md5 == old_md5:
        return "equality"
    else:
        return "inequality"
'''

'''
def find_dir(path,string):

    for filename in os.listdir(path):

        if string in filename:
            return 'not_null'
        else:
            return 'null'
'''