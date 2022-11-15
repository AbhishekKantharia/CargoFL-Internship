#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-06-06 15:02
# @Author  : Vassago
# @File    : test_docker_login.py
# @Software: PyCharm


import logging

from unit_tests.common import BaseTestCase

LOG = logging.getLogger(__name__)


class FlaskrTestDdockerLogin(BaseTestCase):
    def setUp(self):
        self.create_test_app()

    def test_create_user_apikey_and_auth(self):
        status, test_user_openapi_key = self.post('/v1/login', {"username": "vonsago", "password": "Vassago4206"})
        self.assertEqual(status, 200)
        #self.assertxDictContainsEqual(test_user_openapi_key, 'name', "test_user_apikey_test1")
