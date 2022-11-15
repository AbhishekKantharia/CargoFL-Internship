#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-06-09 15:17
# @Author  : Vassago
# @File    : docker_images_api.py
# @Software: PyCharm

from flask import Blueprint
from app.images.docker_images import build_images, search_image, list_images, delete_images


dockerimages_management = Blueprint("docker_images", __name__)

dockerimages_management.add_url_rule(
    rule="/v1/images/build",
    endpoint="images build",
    view_func=build_images,
    methods=["POST"]
)

dockerimages_management.add_url_rule(
    rule="/v1/images",
    endpoint="images list",
    view_func=list_images,
    methods=["GET"]
)

dockerimages_management.add_url_rule(
    rule="/v1/images/search",
    endpoint="images search",
    view_func=search_image,
    methods=["POST"]
)

dockerimages_management.add_url_rule(
    rule="/v1/images/<short_id>",
    endpoint="images delete_images",
    view_func=delete_images,
    methods=["DELETE"]
)