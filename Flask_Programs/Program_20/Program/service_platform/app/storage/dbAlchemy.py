#!/usr/bin/env python
# coding=utf-8
'''
> File Name: dbAlchemy.py
> Author: vassago
> Mail: f811194414@gmail.com
> Created Time: 五  8/10 18:52:51 2018
'''

import logging

from sqlalchemy import create_engine, orm

from app.models.base import Base

LOG = logging.getLogger(__name__)


class SQLAlchemy(object):
    def __init__(self, database_url=None, echo=False):
        self.engine = None
        self.session = None
        self.Model = None

        if database_url:
            self.update_engine(database_url, echo)

    def update_engine(self, database_url, echo):
        self.engine = create_engine(database_url,
                                    pool_recycle=3600,
                                    max_overflow=500,
                                    pool_size=30,
                                    echo=echo)
        self.Model = self.create_base_model()
        self.session = self.create_session()

    def create_base_model(self):
        base = Base
        return base

    def create_session(self, options=None):
        def get_scopefunc():
            try:
                from greenlet import getcurrent as get_ident
            except ImportError:
                # py3 please!
                from threading import get_ident
            return get_ident

        if not options:
            options = {}
        options['expire_on_commit'] = False
        scopefunc = options.pop("scopefunc", get_scopefunc())
        options.setdefault('query_cls', self.Model.query_class)
        return orm.scoped_session(orm.sessionmaker(bind=self.engine, **options), scopefunc)

    def get_session(self):
        class AutoSession(object):
            def __init__(self, session):
                self.session = session
                self.span = None
                self.transaction = None

            def __enter__(self):
                # see http://docs.sqlalchemy.org/en/latest/orm/session_transaction.html
                self.transaction = self.session.begin_nested()
                ScopedSessionTracer.before_session(self.session, self.transaction)
                return self.session

            def __exit__(self, type, value, trace):
                try:
                    result = False
                    if type is None:
                        self.session.commit()
                        result = True
                        if self.transaction.nested and not self.transaction._parent.nested:
                            # LOG.debug("top nested session: commit")
                            self.session.commit()
                    else:
                        self.session.rollback()
                except Exception as e:
                    raise e
                finally:
                    ScopedSessionTracer.after_session(self.session, result)

        return AutoSession(self.session)

    def create_all(self):
        Base.metadata.create_all(self.engine)

    def drop_all(self):
        Base.metadata.drop_all(self.engine)

