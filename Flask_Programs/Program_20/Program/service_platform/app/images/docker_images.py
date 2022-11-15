#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-06-09 15:15
# @Author  : Vassago
# @File    : docker_images.py
# @Software: PyCharm


import logging
from flask import request, jsonify, g
from app.api_exception import ConflictException
from app.docker_client.docker_ops import DockerClient

LOG = logging.getLogger(__name__)

def build_images():
    data = request.get_json()
    dockerfile = data.get("dockerfile")
    name = data.get("name")
    if not dockerfile:
        raise ConflictException("dockerfile can't be none")

    with DockerClient() as docker:
        image = docker.build_image(dockerfile, name)
        LOG.info("build image result", image)
    return jsonify({}), 200


def search_image():
    pass


def list_images():
    result = []
    with DockerClient() as docker:
        images = docker.list_images()
        for image in images:
            for tag in image.tags:
                result.append(
                    {
                        "short_id": image.short_id.split(":")[-1],
                        "tag": tag.split(":")[-1],
                        "repository": tag.split(":")[0],
                        "created": image.attrs.get("Created"),
                        "size": int(image.attrs.get("Size")/1024/1024)
                    }
                )
    return jsonify(result), 200

def delete_images(short_id):
    with DockerClient() as docker:
        if docker.delete_image(short_id):
            return jsonify({}), 200
        else:
            return jsonify({}), 500