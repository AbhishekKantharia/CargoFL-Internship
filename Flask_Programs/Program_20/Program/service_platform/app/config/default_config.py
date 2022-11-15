#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/8 下午9:22
# @Author  : Vassago
# @File    : default_config.py
# @Software: PyCharm

import os

class DefaultConfig():
    CONFIG_NAME = 'DEFAULT'
    DEBUG = True
    TEMPLATE_DIR = "."
    STATIC_DIR = "."

class DevConfig():
    CONFIG_NAME = 'PRO'
    DEBUG = True
    TEMPLATE_DIR = "./app"
    STATIC_DIR = "./app"