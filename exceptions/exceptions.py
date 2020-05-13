from werkzeug.exceptions import HTTPException


class ServerException(Exception):
    code = 500


class InvalidArgument(ServerException):
    code = 400


class ArgumentRequired(ServerException):
    code = 403


class ObjectsDuplicated(ServerException):
    code = 403


class ObjectsNotExisted(ServerException):
    code = 404


class InvalidPattern(ServerException):
    code = 403
