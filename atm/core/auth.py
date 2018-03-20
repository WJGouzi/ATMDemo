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

def userLoginAction(userAccount):
    '''
    用户登录的操作
    :param userAccount 用户的信息
    '''
    print(userAccount)
    retryCount = 0
    while retryCount < 3 and userAccount['isAuthentic'] is not True:
        user = input('请输入账号:').strip()
        password = input('请输入密码:').strip()
        print('user is : %s, password is %s' % (user, password))
        auth = userAuthenticAction(user, password)

    else:
        print('您输入的次数过多')

def userAuthenticAction(userId, userPassword):
    '''
    用户信息的验证
    :param userId: 用户的账号
    :param userPassword: 用户的密码
    :return: 如果验证成功就讲用户对象进行返回，如果验证失败就返回None
    '''
    # 从文件中或者是数据库中读取数据进行验证



