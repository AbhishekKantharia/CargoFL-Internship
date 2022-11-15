#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-06-09 14:28
# @Author  : Vassago
# @File    : test_instance.py
# @Software: PyCharm


import logging

from unit_tests.common import BaseTestCase

LOG = logging.getLogger(__name__)


class TestInstance(BaseTestCase):
    def setUp(self):
        self.short_id = None
        self.create_test_app()

    def test_create_instance(self):
        data = {
            "image": "mysql:5.7.19",
            "ports": "",
            "type": "mysql",
            "volumes": "",
            "environment": ""
        }

        status, testcreateresponse = self.post('/v1/instances', data=data)
        self.assertEqual(status, 200)
        self.short_id = testcreateresponse.get("short_id")
        #self.assertxDictContainsEqual(test_user_openapi_key, 'name', "test_user_apikey_test1")

    def test_get_instance_list(self):
        status, testgetinstance = self.get('/v1/instances')
        self.assertEqual(status, 200)


    def test_restart_instance(self):
        status, testrestartinstance = self.post('/v1/instances/{}/restart'.format(self.short_id))
        self.assertEqual(status, 200)


    def test_stop_instance(self):
        status, teststopinstnace = self.delete('/v1/instances/{}/stop'.format(self.short_id))
        self.assertEqual(status, 200)

