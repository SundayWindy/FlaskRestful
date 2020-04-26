from werkzeug.exceptions import HTTPException


class ServerException(Exception):
    code = 500


class InvalidArgumentException(ServerException):
    code = 400
