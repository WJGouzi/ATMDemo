#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@author: wj
@license: (C) Copyright 2013-2018.
@contact: 1693841903@qq.com
@file: accountsInfo.py
@version: 1.0
@time: 2018/3/21 11:47
@desc: 查询更改用户信息的逻辑
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
from core import dbHandler


def checkUserCurrentBasicInfo(userId):
    '''
    查询用户当前时刻的账户的一些基本信息
    :param userId:
    :return:
    '''
    dbExecute = dbHandler.dbHandler()
    data = dbExecute("select * from accounts where account=%s" % userId)
    return data


def updateUserCurrentBasicInfo(userData):
    '''
    更新当前用户的一些信息
    :param userData: 用户的信息
    :return:
    '''
    dbExcute = dbHandler.dbHandler()
    dbExcute("update accounts where account=%s" % userData['id'], account_data=userData)
    return True
