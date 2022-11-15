#!/usr/bin/env python
# coding=utf-8
'''
> File Name: adapter.py
> Author: vassago
> Mail: f811194414@gmail.com
> Created Time: 四  8/30 16:27:55 2018
'''
from flask import Flask, g, request, jsonify
import json
import requests

LOG = logging.getLogger(__name__)

service_adapter = Flask('service_adapter')


