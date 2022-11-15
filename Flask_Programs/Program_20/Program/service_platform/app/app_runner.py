#!/usr/bin/env python
# coding=utf-8
'''
> File Name: app_runner.py
> Author: vassago
> Mail: f811194414@gmail.com
> Created Time: 一  8/27 22:03:18 2018
'''
import logging
from uuid import uuid4

from flask import Flask, g, request
from flask_cors import *
from werkzeug.exceptions import HTTPException, InternalServerError
from werkzeug.wrappers import Response

from flask_bootstrap import Bootstrap
# from flask_wtf.csrf import CSRFProtect

from app.utils.local import thread_local
from app.storage.database import create_db, db
from app.config.common import config
from app.utils.api_exception import APIException, HttpApiException


LOG = logging.getLogger(__name__)


def configure_models():
    pass

def configure_blueprints(flask_app):
    from app.instance.instance_api import instance_management
    from app.dashboard.dashboard_api import dashboard_management
    from app.images.docker_images_api import dockerimages_management

    flask_app.register_blueprint(instance_management)
    flask_app.register_blueprint(dashboard_management)
    flask_app.register_blueprint(dockerimages_management)

def add_app_hook(app):
    @app.errorhandler(APIException)
    def handler_api_exception(exception):
        return http_error_handler(exception)

    @app.errorhandler(Exception)
    def handler_all_exception(exception):
        return http_error_handler(exception)

    # fixme when flask >0.12. https://github.com/pallets/flask/blob/master/tests/test_user_error_handler.py#L151
    def http_error_handler(exception: Exception) -> Response:
        user_name = getattr(getattr(g, 'user', 'no login'), 'name', 'no login')
        LOG.exception(
            "http_error_handler: InternalServerError user: {} method: {} Url: {}, Body: {}".format(user_name,request.method,request.url,request.get_data()))
        #TODO need db ?
        #db.session.remove()
        if isinstance(exception, APIException):
            response = exception.get_respose()
        elif isinstance(exception, HTTPException):
            response = HttpApiException(exception).get_respose()
        else:

            exception = InternalServerError(str(exception))
            response = HttpApiException(exception).get_respose()

        LOG.info("http_error_handler finish handler error: {response} ".format(response=response))

        return response

    from werkzeug.exceptions import default_exceptions
    for code in default_exceptions:
        app.errorhandler(code)(http_error_handler)

def create_app():
    import app.utils.logger

    flask_app = Flask('psp-controller', template_folder=config.get_template_file_full_path('templates'),
                      static_folder=config.get_static_file_full_path('static'))
    flask_app.config.update(dict(
        SECRET_KEY="powerful secretkey",
        WTF_CSRF_SECRET_KEY="a csrf secret key"
    ))
    # csrf = CSRFProtect(flask_app)
    # csrf.init_app(flask_app)
    CORS(flask_app, supports_credentials=True)
    Bootstrap(flask_app)
    with flask_app.app_context():
        configure_blueprints(flask_app)

    add_app_hook(flask_app)
    return flask_app


if __name__ == "__main__":
    app = create_app()
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    try:
        app.run('0.0.0.0', 5000, debug=app.config["DEBUG"], threaded=True)
    except Exception as e:
        LOG.info("Program exit unexpectly because an error {}".format(e))
