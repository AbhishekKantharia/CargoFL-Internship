#!/usr/bin/env python
# coding=utf-8
'''
> File Name: docker_ops.py
> Author: vassago
> Mail: f811194414@gmail.com
> Created Time: 二  8/28 10:08:15 2018
'''
from __future__ import absolute_import
import docker
import logging

LOG = logging.getLogger(__name__)

class DockerClient():
    def __init__(self):
        self.client = None
        self.has_login = False

    def __enter__(self):
        if self.client:
            LOG.info("docker service is already exesit!")
            return self
        try:
            self.client = docker.from_env()
            LOG.info("docker service is available: {}".format(self.client.version()))
            return self
        except Exception as e:
            LOG.info("docker service is not available: {}".format(e))
    
    def __exit__(self, exc_ty, exc_val, tb):
        if self.client:
            self.client.close()
        self.client = None

    def login(self, username, password, registry, **kwargs):
        if not self.client:
            return False
        return self.client.login(username=username, password=password, registry=registry if registry else "https://index.docker.io/v1/")

    def version(self):
        return self.client.version()

    def pull_images(self, images):
        images = [self.client.images.pull(im) for im in images]
        LOG.info("pull images: {} succeed".format(images))
        return images

    def list_containers(self):
        return self.client.containers.list()

    def list_images(self):
        return self.client.images.list()

    def exsit_image(self, image_tag):
        for image in self.list_images():
            if image_tag in image.tags:
                LOG.info("image: {} is already pulled".format(image_tag))
                return True
        return False

    def exsit_container(self, image_tag):
        for container in self.list_containers():
            if image_tag in container.image.tags:
                LOG.info("container: {} is already running".format(image_tag))
                return True
        return False

    def get_image_tag_status(self, image_tag):
        pass

    def get_container(self, image_tag):
        for container in self.list_containers():
            if image_tag in container.image.tags:
                return container
        return None

    def run(self, image_tag, ports, volumes, environment=None, backend=True):
        if not self.exsit_image(image_tag):
            self.pull_images([image_tag])

        if self.exsit_container(image_tag):
            return self.get_container(image_tag)

        if backend:
            container = self.client.containers.run(image_tag, ports=ports,
                    volumes=volumes, detach=True, environment=environment)
            LOG.info("container: {} running in backend| detail:{},{}".format(image_tag,ports,volumes))
            return container

    def stop(self, image_meta, stop_all = False):
        for container in self.list_containers():
            if stop_all and "vonsago/psp" not in container.image.tags[0]:
                container.stop()
                LOG.info("stop one of all container")
            elif image_meta in container.image.tags or image_meta == container.short_id:
                container.stop()
                LOG.info("stop {} success".format(image_meta))
                return True
        return False

    def restart(self, short_id):
        for container in self.list_containers():
            if short_id == container.short_id:
                container.restart()
        return True

    def build_image(self, dockerfile, name):
        image = self.client.images.build(path=dockerfile, tag=name, rm=True, nocache=True)
        return image

    def delete_image(self, short_id):
        try:
            self.client.images.remove(image=short_id)
        except Exception as e:
            LOG.info(e)
            return False
        return True