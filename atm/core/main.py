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
from core import transaction

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
        2.  还款
        3.  取款
        4.  转账
        5.  账单
        6.  退出
        \033[0m'''

    choiceMenu = {
        '1': showUserAccountInfo,
        '2': repay,
        '3': withdrawingMoney,
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
            print("\033[31;1m 选项不存在! \033[0m")


########################### 用户的一些交互的行为 #####################################

def showUserAccountInfo(userAccountData):

    print("\033[32;1m---------User info----------------\033[0m")
    for (key, value) in userData.items():
        if key == 'userData':
            for (infoKey, infoValue) in userData['userData'].items():
                print(infoKey, '---', infoValue)
        else:
            print(key, '---', value)


@loginAuthentic
def repay(userAccountData):
    '''
    还款的逻辑
    :param userAccountData: 用户的账户信息
    :return:
    '''
    currentUserBasicInfo = accountsInfo.checkUserCurrentBasicInfo(userAccountData['userID'])
    currentMoney = '''
        \033[32;1m_________________ basic info ________________________
        信用额度 : %.2f 
        可用余款 : %.2f \033[0m''' % (float(currentUserBasicInfo['credit']), float(currentUserBasicInfo['balance']))
    print(currentMoney)

    backFlag = False

    while not backFlag:
        repayMoney = input('''\033[32;1m请输入还款的金额(返回上级菜单请按【b】):\033[0m''').strip()
        if len(repayMoney) > 0 and (repayMoney.isdigit() or isJudgeFloat(repayMoney)):
            '''
            输入金额有效
            '''
            newUserInfo = transaction.transactionAction(currentUserBasicInfo, 'repay', repayMoney)
            if newUserInfo:
                print('''\033[32;1m现在账户的余额为:%.2f\033[0m''' % float(newUserInfo['balance']))
        elif repayMoney == 'b':
            backFlag = True
        else:
            print('\033[31;1m[%s] 输入的数据无效 \033[0m' % repayMoney)


def withdrawingMoney(userAccountData):
    '''
    取款的逻辑
    :param userData: 用户的账户信息
    :return:
    '''
    currentUserBasicInfo = accountsInfo.checkUserCurrentBasicInfo(userAccountData['userID'])
    currentMoney = '''
        \033[32;1m_________________ basic info ________________________
        信用额度 : %.2f 
        可用余款 : %.2f \033[0m''' % (float(currentUserBasicInfo['credit']), float(currentUserBasicInfo['balance']))
    print(currentMoney)
    backFlag = False
    while not backFlag:
        withdrawMoney = input('''\033[32;1m请输入取款的金额(返回上级菜单请按【b】):\033[0m''').strip()
        print(withdrawMoney.isdigit(), withdrawMoney.isdecimal())
        if len(withdrawMoney) > 0 and (withdrawMoney.isdigit() or isJudgeFloat(withdrawMoney)):
            '''
            输入的金额是有效的
            '''
            newUserInfo = transaction.transactionAction(currentUserBasicInfo, 'withdraw', withdrawMoney)
            if newUserInfo:
                print('''\033[32;1m现在账户的余额为:%.2f\033[0m''' % float(newUserInfo['balance']))
        elif withdrawMoney == 'b':
            backFlag = True
        else:
            print('\033[31;1m[%s] 输入的数据无效 \033[0m' % withdrawMoney)
        pass




def isJudgeFloat(inputValue):
    '''
    判断输入的内容是否为一个小数
    :param inputValue: 输入的内容
    :return: 返回True表示为小数，False则不是小数
    '''
    str1 = str(inputValue)
    if str1.count('.') > 1:  # 判断小数点是不是大于1
        return False
    elif str1.isdigit():
        return False  # 判断是不是整数
    else:
        new_str = str1.split('.')  # 按小数点分割字符
        frist_num = new_str[0]  # 取分割完之后这个list的第一个元素
        if frist_num.count('-') > 1:  # 判断负号的格数，如果大于1就是非法的
            return False
        else:
            frist_num = frist_num.replace('-', '')  # 把负号替换成空
    if frist_num.isdigit() and new_str[1].isdigit():
        # 如果小数点两边都是整数的话，那么就是一个小数
        return True
    else:
        return False