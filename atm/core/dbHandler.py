#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@author: wj
@license: (C) Copyright 2013-2018.
@contact: 1693841903@qq.com
@file: dbHandler.py
@version: 1.0
@time: 2018/3/21 09:20
@desc: 数据库操作相关的逻辑
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
             ┏┓     ┏┓
            ┏┛┻━━━━━┛┻┓
            ┃    ☃    ┃
            ┃  ┳┛  ┗┳  ┃
            ┃    ┻     ┃
            ┗━┓     ┏━━┛
              ┃     ┗━━━━┓
              ┃  神兽保佑  ┣┓
              ┃　永无BUG！  ┏┛
              ┗┓┓┏━━━━━┳┓┏┛
               ┃┫┫     ┃┫┫
               ┗┻┛     ┗┻┛
"""
import os
import sys
import json

# sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from conf import settings

def dbHandler():
    '''
    数据库的操作
    :return:
    '''
    connectParams = settings.DATABASE
    print(connectParams)

    if connectParams['engine'] == 'file_storage':
        return dbHandlerInFile(connectParams)
    elif connectParams['engine'] == 'mysql':
        pass


def dbHandlerInFile(connectParams):
    print('file db:', connectParams)
    return file_execute

def file_execute(sql, **kwargs):
    conn_params = settings.DATABASE
    db_path = '%s/%s' % (conn_params['path'], conn_params['name'])

    print(sql,db_path)
    sql_list = sql.split("where")
    print(sql_list)
    if sql_list[0].startswith("select") and len(sql_list) > 1: #has where clause
        column,val = sql_list[1].strip().split("=")

        if column == 'account':
            account_file = "%s/%s.json" % (db_path, val)
            print('account file path is : %s' % account_file)
            if os.path.isfile(account_file):
                with open(account_file, 'r') as f:
                    account_data = json.load(f)
                    print('account data is : ' , account_data)
                    return account_data
            else:
                exit("\033[31;1mAccount [%s] does not exist!\033[0m" % val)

    elif sql_list[0].startswith("update") and len(sql_list)> 1:#has where clause
        column, val = sql_list[1].strip().split("=")
        if column == 'account':
            account_file = "%s/%s.json" % (db_path, val)
            #print(account_file)
            if os.path.isfile(account_file):
                account_data = kwargs.get("account_data")
                with open(account_file, 'w') as f:
                    acc_data = json.dump(account_data, f)
                    print(acc_data)
                return True