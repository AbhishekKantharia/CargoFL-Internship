#!/usr/bin/env python
# coding=utf-8
'''
> File Name: logger.py
> Author: vassago
> Mail: f811194414@gmail.com
> Created Time: 三  8/29 18:59:32 2018
'''
import logging
import os
import warnings

from app.config.common import config

log_level = logging.INFO
if os.getenv('APP_LOG_LEVEL', log_level) == "INFO":
    log_level = logging.INFO

logging.basicConfig(level=log_level, format='%(asctime)s %(name)s %(levelname)-8s %(message)s')
logging.getLogger("app").setLevel(log_level)
warnings.simplefilter("once")
logging.getLogger('requests.packages.urllib3.connectionpool').setLevel(logging.ERROR)
logging.getLogger('urllib3.connectionpool').setLevel(logging.ERROR)


logging.getLogger('sqlalchemy.engine').setLevel(logging.ERROR)
logging.getLogger("requests.packages.urllib3").setLevel(logging.ERROR)
logging.getLogger('app.utils.requests_log').setLevel(logging.ERROR)
