#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/8 下午9:04
# @Author  : Vassago
# @File    : api_exception.py
# @Software: PyCharm

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from flask import Response


class APIException(Exception):

    def __init__(self, status_code=None, msg=None, error_id=None, message=None):
        '''

        :param status_code:
        :param msg: deprecated ,use message
        :param error_id:
        :param message:
        '''
        self.status_code = status_code
        if msg:
            self.error_info = msg
        else:
            self.error_info = message
        self.error_type = error_id

    def get_respose(self):
        return Response(response=json.dumps({"error_info": str(self.error_info), "error_type": self.error_type}),
                        status=self.status_code, mimetype="application/json")


class BadRequestException(APIException):
    def __init__(self, message=None):
        APIException.__init__(self, 400, error_id='error_bad_request', message=message)


class ConflictException(APIException):
    def __init__(self, message=None):
        APIException.__init__(self, 409, error_id='error_already_exists', message=message)


class UnAuthenticatedException(APIException):
    def __init__(self, message=None):
        APIException.__init__(self, 401, error_id='error_unauthenticated', message=message)


class ForbiddenException(APIException):
    def __init__(self, message=None):
        APIException.__init__(self, 403, error_id='error_permission', message=message)


class NotFoundException(APIException):
    def __init__(self, message=None):
        APIException.__init__(self, 404, error_id='error_not_found', message=message)


class InternalServerError(APIException):
    def __init__(self, message=None):
        APIException.__init__(self, 500, error_id='Internal Server Error', message=message)


class HttpApiException(APIException):
    '''
    transform werkzeug.exceptions.HTTPException
    '''

    def __init__(self, http_exception):
        APIException.__init__(self, http_exception.code, error_id=http_exception.name,
                              message=getattr(http_exception, 'description', http_exception.name))
