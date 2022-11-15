#!/usr/bin/env python
# coding=utf-8
'''
> File Name: base_config.py
> Author: vassago
> Mail: f811194414@gmail.com
> Created Time: 三  8/29 19:17:17 2018
'''
import os

def str2bool(v):
    if v is None or isinstance(v, bool):
        return v
    return v.lower() in ("yes", "true", "t", "1")

def str2int(v):
    if v is None:
        return v
    if v is '':
        return None
    return int(v)

def str2float(v):
    if v is None:
        return v
    return int(v)


MAIN_DIRECTORY = os.path.dirname(os.path.dirname(__file__))


def get_full_path(*path):
    return os.path.abspath(os.path.join(MAIN_DIRECTORY, *path))

class Base():
    CONFIG_NAME = 'BASE'
    MAIN_DIRECTORY = MAIN_DIRECTORY
    PROD = str2bool(os.getenv('PROD', "True"))
    SERVICE_NAME = os.getenv('SERVICE_NAME', "csp_controller")

    SECRET_KEY = "powerful secretkey fff",
    WTF_CSRF_SECRET_KEY = "a csrf secret key"

    # ALL,WORKER,CONTROLLER
    RUN_MODEL = os.getenv('RUN_MODEL', "CONTROLLER")
    TZ = os.getenv('TZ', "Asia/Shanghai")

    DATABASE_MYSQL_URL = os.getenv("DATABASE_MYSQL_URL", "root:root@localhost:3306/psp")
    DATABASE_URL = os.getenv("DATABASE_URL", "mysql+pymysql://{}?charset=utf8mb4".format(DATABASE_MYSQL_URL))
    DATABASE_URL_ENCODING = os.getenv('DATABASE_URL_ENCODING', "utf8mb4")
