#!/usr/bin/env python
# coding=utf-8
'''
> File Name: instance_api.py
> Author: vassago
> Mail: f811194414@gmail.com
> Created Time: 三  8/29 19:53:13 2018
'''

from flask import Blueprint
from .instance import instance_create_view, list_instances, stop_instance, restart_instance

instance_management = Blueprint("instance_management", __name__)

instance_management.add_url_rule(
        rule="/v1/instances",
        endpoint="create_instance",
        view_func=instance_create_view,
        methods=["POST"]
        )

instance_management.add_url_rule(
        rule="/v1/instances",
        endpoint="list_instances",
        view_func=list_instances,
        methods=["GET"]
        )

instance_management.add_url_rule(
        rule="/v1/instances/<instance_id>/stop",
        endpoint="stop_instance",
        view_func=stop_instance,
        methods=["DELETE"]
        )

instance_management.add_url_rule(
        rule="/v1/instances/<instance_id>/restart",
        endpoint="restart_instance",
        view_func=restart_instance,
        methods=["POST"]
        )