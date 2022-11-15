#!/usr/bin/env python
# coding=utf-8
'''
> File Name: schema.py
> Author: vassago
> Mail: f811194414@gmail.com
> Created Time: 六  9/29 17:52:07 2018
'''

from marshmallow import Schema, fields  

class InstanceSchema(Schema):
    name = fields.String(required=True)
    short_id = fields.String(required=True)
    status = fields.String(required=True)
    created = fields.String(required=True)

