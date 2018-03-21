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
from core.auth import loginAuthentic
from core import  accountsInfo

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
    return auth.userLoginAction(userData)



def run():
    data = userLoginAction()
    # 验证通过的话就进行交互
    if userData['isAuthentic'] == True:
        userData['userData'] = data
        interactionWithUserAccout(userData)

def interactionWithUserAccout(userAccount):
    '''
    用户的一些操作
    :param userAccount: 用户的账户信息
    :return:
    '''

    menu = u'''
        ------- wangjun Bank ---------
        \033[32;1m1.  账户信息
        2.  还款(功能已实现)
        3.  取款(功能已实现)
        4.  转账
        5.  账单
        6.  退出
        \033[0m'''

    choiceMenu = {
        '1': showUserAccountInfo,
        '2': repay,
        '3': '',
        '4': '',
        '5': '',
        '6': '',
    }

    exitFlag = False
    while not exitFlag:
        print(menu)
        choice = input('>>>').strip()
        if choice in choiceMenu:
            choiceMenu[choice](userAccount)
        else:
            print("\033[31;1mOption does not exist!\033[0m")


########################### 用户的一些交互的行为 #####################################

def showUserAccountInfo(userAccountData):

    print("\033[32;1m---------User info----------------\033[0m")
    print(userData)

@loginAuthentic
def repay(userAccountData):
    currentUserBasicInfo = accountsInfo.checkUserCurrentBasicInfo(userData['userID'])
    print(currentUserBasicInfo)
