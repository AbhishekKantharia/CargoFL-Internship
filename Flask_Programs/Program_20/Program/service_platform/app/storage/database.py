#!/usr/bin/env python
# coding=utf-8
'''
> File Name: database.py
> Author: vassago
> Mail: f811194414@gmail.com
> Created Time: 五  8/10 18:57:22 2018
'''

from contextlib import contextmanager
import logging

from alembic import command
from alembic.config import Config
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import create_database
from app.config.common import config
from app.models.base import Base
from app.storage.dbAlchemy import SQLAlchemy

LOG = logging.getLogger(__name__)

db = SQLAlchemy()


@contextmanager
def global_sqlalchemy_session():
    '''
    每次都是一个单独的session
    :return:
    '''
    session = sessionmaker(bind=db.engine, expire_on_commit=False)()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.expunge_all()
        session.close()


def sqlalchemy_session():
    """
    scoped_session
    用法:
        1.每次with都开一个子事务,退出顶层with进行提交，内部请用session.flush()提交到数据库（只在本事务内能看到效果），禁止事务内使用commit()
    例:
    with sqlalchemy_session as session:
        do1
        with sqlalchemy_session as session2:
            do2()
        with sqlalchemy_session as session2:
            do3()
    :param rollcack_and_new_session: 默认为false，如果为true，会回滚之前的session，并开一个新的session
    :return:

    """
    return db.get_session()


def init_app_webhook(app):
    # 每次请求完成后,自动提交session
    @app.after_request
    def after_clean(resp, *args, **kwargs):
        db.session.commit()
        return resp

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db.session.remove()


def create_database(db_url, encoding):
    from sqlalchemy_utils import database_exists, create_database as origin_create_database
    if database_exists(config.DATABASE_URL):
        return

    if 'mysql' in db_url:
        origin_create_database(db_url, encoding)
    else:
        origin_create_database(db_url)


def create_db(app=None):
    create_database(config.DATABASE_URL, config.DATABASE_URL_ENCODING)
    db.update_engine(config.DATABASE_URL, echo=config.SHOW_SQL)
    if app:
        init_app_webhook(app)


def init_db():
    if not config.DB_MIGRATION:
        Base.metadata.create_all(db.engine)
    else:
        alembic_cfg = Config(config.ALEMBIC_CONFIG)
        alembic_cfg.set_main_option('script_location', config.ALEMBIC_SCRIPT_LOCATION)
        command.upgrade(alembic_cfg, "head")
        command.stamp(alembic_cfg, "head")

