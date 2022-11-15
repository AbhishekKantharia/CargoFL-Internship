#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-06-09 15:12
# @Author  : Vassago
# @File    : test_build_image.py
# @Software: PyCharm


import logging

from unit_tests.common import BaseTestCase

LOG = logging.getLogger(__name__)


class TestImages(BaseTestCase):
    def setUp(self):
        self.create_test_app()

    def test_build_images(self):
        data = {
            "dockerfile": "/Users/vassagovon/myProject/venv_PSP/service_platform/Dockerfile",
            "name": "vonsago/psp:3.0"
        }
        status, testbuildimages = self.post('/v1/images/build', data=data)
        self.assertEqual(status, 200)
        #self.assertxDictContainsEqual(test_user_openapi_key, 'name', "test_user_apikey_test1")

    def test_get_images(self):
        pass

    def test_search_image(self):
        pass

    def test_pull_image(self):
        pass

