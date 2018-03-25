#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = '关于打印输出相关的逻辑'
__author name__ = 'gouzi'
__create time__ = '2018/3/25'
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


import logging
from conf import settings

def loggerAction(logType):
    '''
    打印日志的操作
    :param logType: 打印日志的输出的级别
    '''
    loggerObject = logging.getLogger(logType)
    loggerObject.setLevel(settings.LOGGINGLEVEL)

    ch = logging.StreamHandler()
    ch.setLevel(settings.LOGGINGLEVEL)

    filePath = '%s/log/%s'% (settings.basePath, settings.LOGGINGTYPE[logType])
    fh = logging.FileHandler(filePath)
    fh.setLevel(settings.LOGGINGLEVEL)

    screenAndFileFommater = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(screenAndFileFommater)
    fh.setFormatter(screenAndFileFommater)

    loggerObject.addHandler(ch)
    loggerObject.addHandler(fh)

    return loggerObject



