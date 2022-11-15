#!/usr/bin/env python
# coding=utf-8
'''
> File Name: base.py
> Author: vassago
> Mail: f811194414@gmail.com
> Created Time: 四  8/30 15:44:25 2018
'''

import time
import logging
from sqlalchemy import Boolean, Column, orm
from sqlalchemy.orm.query import Query
from sqlalchemy.dialects.mysql import DOUBLE
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.base import _generative
from flask import request

LOG = logging.getLogger(__name__)


class _Model(object):
    created_at = Column(DOUBLE, nullable=False, default=lambda: time.time())
    updated_at = Column(DOUBLE, nullable=False, default=lambda: time.time(), onupdate=lambda: time.time())
    deleted_at = Column(DOUBLE, nullable=False, default=lambda: time.time())
    deleted = Column(Boolean, default=False, index=True)

    def delete(self):
        self.deleted_at = time.time()
        self.deleted = True


class _Query(Query):
    """
    see: https://bitbucket.org/zzzeek/sqlalchemy/wiki/UsageRecipes/PreFilteredQuery
    默认过滤is_deleted 或deleted 为true的记录
    """
    _with_deleted = False

    def get(self, ident):
        # override get() so that the flag is always checked in the
        # DB as opposed to pulling from the identity map. - this is optional.
        return Query.get(self.populate_existing(), ident)

    def __iter__(self):
        return Query.__iter__(self.custom_filter())

    def from_self(self, *ent):
        # override from_self() to automatically apply
        # the criterion too.   this works with count() and
        # others.
        return Query.from_self(self.custom_filter(), *ent)

    def custom_filter(self):
        mzero = self._mapper_zero()
        if mzero is not None:
            if not self._with_deleted:
                # LOG.debug("_with_deleted is not true, add deleted=False")
                if hasattr(mzero.class_, 'deleted'):
                    crit = mzero.class_.deleted.is_(False)
                    return self.enable_assertions(False).filter(crit)
        return self

    @_generative(orm.Query._no_statement_condition)
    def with_deleted(self):
        # LOG.debug("change _with_deleted to true")
        self._with_deleted = True

    """
    Base Query: 可以自定义查询方法

    Example:
        User.query.paginate(page=2, per_page=10, error_out=False)
    """

    @_generative(orm.Query._no_statement_condition)
    def paginate(self, limit=10000000, offset=0):
        limit, offset = 10000000, 0
        if request and request.args:
            limit = int(request.args.get('limit', 10000000))
            offset = int(request.args.get('offset', 0))
        self._limit = limit
        self._offset = offset


Base = declarative_base(cls=_Model, name="Model")

if not getattr(Base, 'query_class', None):
    Base.query_class = _Query
