#!/usr/bin/env python
# coding=utf-8
'''
> File Name: common.py
> Author: vassago
> Mail: f811194414@gmail.com
> Created Time: 三  8/29 19:16:04 2018
'''


import logging

import os

LOG = logging.getLogger(__name__)
from .base_config import str2bool


class Config():
    def __init__(self):
        self.config = None
        self.get_config()

    def get_config(self, config_name=os.getenv("CONFIG_NAME", "DEFAULT")):
        LOG.info("config use: %s", config_name)
        if config_name == "DEFAULT":
            from .default_config import DefaultConfig
            self.config = DefaultConfig()
        else:
            from .default_config import DevConfig
            self.config = DevConfig()
        return self

    def __getattr__(self, item):
        return getattr(self.config, item)

    def get_full_path(self, *path):
        return os.path.abspath(os.path.join(self.config.MAIN_DIRECTORY, *path))

    def get_static_file_full_path(self, *path):
        return os.path.abspath(os.path.join(self.config.STATIC_DIR, *path))

    def get_template_file_full_path(self, *path):
        return os.path.abspath(os.path.join(self.config.TEMPLATE_DIR, *path))


config = Config()
