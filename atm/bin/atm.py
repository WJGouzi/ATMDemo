#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = '程序的主入口'
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


from core import main

if __name__ == '__main__':
    main.run()