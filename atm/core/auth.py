#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = '用户的相关认证逻辑'
__author name__ = 'gouzi'
__create time__ = '2018/3/20'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
             ┏┓   ┏┓
            ┏┛┻━━━┛┻━━━┓
            ┃    ☃    ┃
            ┃  ┳┛  ┗┳  ┃
            ┃    ┻     ┃
            ┗━┓      ┏━┛
              ┃      ┗━━━━━━━┓
              ┃   神兽保佑    ┣┓
              ┃    永无BUG！ ┏┛
              ┗┓┓┏━━┳━┓ ┏━━━┛
               ┃┫┫    ┃┫┫
               ┗┻┛    ┗┻┛
"""
import os
import sys
import time

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from core import dbHandler

def userLoginAction(userAccount):
    '''
    用户登录的操作
    :param userAccount 用户的信息
    '''
    print(userAccount)
    retryCount = 0
    while retryCount < 3 and userAccount['isAuthentic'] is not True:
        user = input('\033[32;1m请输入账号:\033[0m').strip()
        password = input('\033[32;1m请输入密码:\033[0m').strip()
        auth = userAuthenticAction(user, password)
        if auth: # 时间也验证通过了
            userAccount['isAuthentic'] = True
            userAccount['userID'] = user
            return auth
        retryCount += 1
    else:
        print('您输入的次数过多')
        exit()

def userAuthenticAction(userId, userPassword):
    '''
    用户信息的验证
    :param userId: 用户的账号
    :param userPassword: 用户的密码
    :return: 如果验证成功就讲用户对象进行返回，如果验证失败就返回None
    '''
    # 从文件中或者是数据库中读取数据进行验证
    dbHandlerWithSQL = dbHandler.dbHandler()
    data = dbHandlerWithSQL("select * from accounts where account=%s" % userId)

    if data['password'] == userPassword: # 说明用户的信息已经被找到了
        '''
        用户的时间有没有过期这些也是需要进行验证
        '''
        expireDateStamp = time.mktime(time.strptime(data['expire_date'], '%Y-%m-%d'))
        if time.time() > expireDateStamp:
            print("\033[31;1mAccount [%s] has expired,please contact the back to get a new card!\033[0m" % userId)
        else:
            return data
    else:
        print("\033[31;1mAccount ID or password is incorrect!\033[0m")


def loginAuthentic(func):
    '''
    验证用户的登录情况
    :param func:
    :return:
    '''
    def wrapper(*args,**kwargs):
        if args[0].get('isAuthentic'):
            return func(*args, **kwargs)
        else:
            exit("User is not authenticated.")
    return wrapper
