#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@author: wj
@license: (C) Copyright 2013-2018.
@contact: 1693841903@qq.com
@file: transaction.py
@version: 1.0
@time: 2018/3/21 14:14
@desc: 交易相关的逻辑
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

from conf import settings
from core import accountsInfo



def transactionAction(userData, dealType, amount, **kwargs):
    '''
    关于交易相关的逻辑处理
    :param userData: 用户的信息
    :param dealType: 交易的类型
    :param amount: 交易的金额
    :param kwargs: 拓展的参数
    :return:
    '''
    amount = float(amount)
    if dealType in settings.TRANSACTION_TYPE:
        if amount > 1000:  # 大于1000以上的才有利息计算
            interest = amount * float(settings.TRANSACTION_TYPE[dealType]['interest'])
        else:
            interest = 0
        oldMoneyAmount = userData['balance']
        if settings.TRANSACTION_TYPE[dealType]['action'] == 'plus':
            newMoneyAmount = oldMoneyAmount + amount + interest
        elif settings.TRANSACTION_TYPE[dealType]['action'] == 'minus':
            newMoneyAmount = oldMoneyAmount - amount - interest
            if newMoneyAmount < 0:
                print('''\033[31;1m您的信用额度为: [%s], 不足以进行此次[-%s]的交易, 您可用的金额为:[%s]''' % (userData['credit'], (amount + interest), oldMoneyAmount))
                return
            else:
                if interest > 0:
                    print("\033[31;1m交易中扣除了相应的手续费为:[%.2f]\033[0m" % interest)
        userData['balance'] = newMoneyAmount
        accountsInfo.updateUserCurrentBasicInfo(userData)
        return userData
    else:
        print("\033[31;1m交易类型 : [%s] 不存在!\033[0m" % dealType)
