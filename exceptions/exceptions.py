from werkzeug.exceptions import HTTPException


class ServerException(Exception):
    code = 500


class InvalidArgumentException(ServerException):
    code = 400


class ArgumentRequiredException(ServerException):
    code = 403


class InvalidPattern(ServerException):
    code = 403
