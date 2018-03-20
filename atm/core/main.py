#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = '程序的主要程序'
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

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from core import auth


'''
用户的信息
'''
userData = {
    'userID' : None,         # 用户的账号
    'userData' : None,       # 用户的相关的数据
    'isAuthentic' : False    # 用户是否验证通过
}



def userLoginAction():
    '''
    这里是让用户进行登录操作的提示
    :return:
    '''
    # 需要进行验证
    auth.userLoginAction(userData)



def run():
    print('main function')
    userLoginAction()
    # 验证通过的话就进行交互

