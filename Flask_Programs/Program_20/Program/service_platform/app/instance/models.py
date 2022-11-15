#!/usr/bin/env python
# coding=utf-8
'''
> File Name: models.py
> Author: vassago
> Mail: f811194414@gmail.com
> Created Time: 三  8/29 19:54:17 2018
'''
import time
from uuid import uuid4

from sqlalchemy import Boolean, Column, Integer, JSON, String, TEXT
from sqlalchemy.dialects.mysql import DOUBLE
from sqlalchemy.orm import relationship

from app.models.base import Base
from sqlalchemy.orm.attributes import flag_modified


class Instance(Base):
    __tablename__ = "instance"
    id = Column(String(255), primary_key=True, default=str(uuid4()))
    name = Column(String(255), nullable=False)
    status = Column(String(255), nullable=False, default="creating")
