#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/8 下午8:57
# @Author  : Vassago
# @File    : dashboard.py
# @Software: PyCharm

from flask import render_template, flash, request, jsonify, g
from app.docker_client.docker_ops import DockerClient

def show_dashboard():
    with DockerClient() as docker:
        if not docker:
            flash("Error: Docker Service Is Not Available !")
    return render_template("index.html")

def docker_login_check_view():
    if True:
        return jsonify({"logined": True}), 200
    return jsonify({}), 200

def docker_login_view():
    login_data = request.get_json()
    username = login_data.get("username")
    password = login_data.get("password")
    registry = login_data.get("registry")
    with DockerClient() as docker:
        try:
            resp = docker.login(username, password, registry)
            setattr(g, "has_docker_login", True)
        except:
            resp = None
            setattr(g, "has_docker_login", False)

        return jsonify(resp if resp else {}), 200
