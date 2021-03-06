#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@author: wj
@license: (C) Copyright 2013-2018.
@contact: 1693841903@qq.com
@file: settings.py
@version: 1.0
@time: 2018/3/21 09:31
@desc: 一些配置文件
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
import logging

basePath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(basePath)

DATABASE = {
    'engine': 'file_storage', #support mysql,postgresql in the future
    'name':'accounts',
    'path': "%s/db" % basePath
}



# 交易的类型
TRANSACTION_TYPE = {
    'repay': {'action': 'plus', 'interest': 0},         # 还款
    'withdraw': {'action': 'minus', 'interest': 0.05},  # 取款
    'transfer': {'action': 'minus', 'interest': 0.05},  # 转账
    'consume': {'action': 'minus', 'interest': 0},      # 消费
}


LOGGINGTYPE = {
    'access': 'access.log',
    'transaction': 'transaction.log'
}

LOGGINGLEVEL = logging.INFO