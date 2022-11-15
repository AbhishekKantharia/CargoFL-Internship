#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/8 下午8:58
# @Author  : Vassago
# @File    : dashboard_api.py
# @Software: PyCharm

from flask import Blueprint
from app.dashboard.dashboard import show_dashboard, docker_login_view, docker_login_check_view

dashboard_management = Blueprint("dashboard", __name__)

dashboard_management.add_url_rule(
        rule="/v1",
        endpoint="dashboard",
        view_func=show_dashboard,
        methods=["GET"]
)

dashboard_management.add_url_rule(
        rule="/v1/login/check",
        endpoint="docker login check",
        view_func=docker_login_check_view,
        methods=["GET"]
)

dashboard_management.add_url_rule(
        rule='/v1/login',
        endpoint="docker login view",
        view_func=docker_login_view,
        methods=["POST"]
)