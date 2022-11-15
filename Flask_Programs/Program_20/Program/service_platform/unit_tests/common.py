#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-06-06 14:36
# @Author  : Vassago
# @File    : common.py
# @Software: PyCharm

import json
import logging
from unittest import TestCase

from app.config import base_config
from app.app_runner import create_app as _create_app

LOG = logging.getLogger(__name__)


class BaseTestCase(TestCase):
    def get_before_run_test_app(self):
        if not hasattr(self, 'app') or not self.app:
            self.app = _create_app()
        return self.app

    def create_test_app(self):
        # config.get_config('TEST')
        # LOG.info("database use:%s", config.DATABASE_URL)
        # if "test" not in config.DATABASE_URL:
        #     LOG.error("please use a db name like 'test_xxx' ,because the testcase will clean the database")
        #     raise Exception(gettext("database name error"))
        # if database_exists(config.DATABASE_URL):
        #     drop_database(config.DATABASE_URL)
        #     create_database(config.DATABASE_URL)
        self.get_before_run_test_app()
        self.app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False
        self.app_client = self.app.test_client()
        self.headers = {'content_type': 'application/json'}

    def get(self, url, data=None, headers=None, check_status=True, query_string=None):
        result_headers = {}
        if not headers:
            headers = {}
        result_headers.update(self.headers)
        result_headers.update(headers)
        rv = self.app_client.get(url, data=data, headers=result_headers, query_string=query_string)
        # LOG.info("get user info %s", json.loads(rv.data))
        if rv.status_code != 404 and rv.status_code >= 400:
            LOG.error("request error %s", json.loads(rv.data))
            if check_status:
                raise self.failureException("http error: {}".format(rv.data))
        return rv.status_code, json.loads(rv.data)

    def post(self, url, data=None, headers=None, check_status=True):
        result_headers = {}
        if not headers:
            headers = {}
        result_headers.update(self.headers)
        result_headers.update(headers)
        if data:
            data = json.dumps(data)
        else:
            data = {}
        rv = self.app_client.post(url, data=data, follow_redirects=True, content_type='application/json',
                                  headers=result_headers)
        # LOG.info("get user info %s", json.loads(rv.data))
        if rv.status_code >= 400:
            LOG.error("request error %s", json.loads(rv.data))
            if check_status:
                raise self.failureException("http error: {}".format(rv.data))
        return rv.status_code, json.loads(rv.data)

    def patch(self, url, data=None, headers=None, check_status=True):
        result_headers = {}
        if not headers:
            headers = {}
        result_headers.update(self.headers)
        result_headers.update(headers)
        rv = self.app_client.patch(url, data=json.dumps(data), follow_redirects=True, content_type='application/json',
                                   headers=result_headers)
        if rv.status_code != 404 and rv.status_code >= 400:
            LOG.error("request error %s", json.loads(rv.data))
            if check_status:
                raise self.failureException("http error: {}".format(rv.data))
        return rv.status_code, json.loads(rv.data)

    def put(self, url, data=None, headers=None, check_status=True):
        result_headers = {}
        if not headers:
            headers = {}
        result_headers.update(self.headers)
        result_headers.update(headers)
        rv = self.app_client.put(url, data=json.dumps(data), follow_redirects=True, content_type='application/json',
                                 headers=result_headers)
        # LOG.info("get user info %s", json.loads(rv.data))
        if rv.status_code != 404 and rv.status_code >= 400:
            LOG.error("request error %s", json.loads(rv.data))
            if check_status:
                raise self.failureException("http error: {}".format(rv.data))
        return rv.status_code, json.loads(rv.data)

    def delete(self, url, headers=None, check_status=True):
        result_headers = {}
        if not headers:
            headers = {}
        result_headers.update(self.headers)
        result_headers.update(headers)
        rv = self.app_client.delete(url, follow_redirects=True, content_type='application/json', headers=result_headers)
        # LOG.info("get user info %s", json.loads(rv.data))
        json_data = None
        if rv.status_code != 404 and rv.status_code >= 400:
            LOG.error("request error %s", json.loads(rv.data))
            if check_status:
                raise self.failureException("http error: {}".format(rv.data))
        if rv.data:
            json_data = json.loads(rv.data)
        return rv.status_code, json_data

