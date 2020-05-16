class ServerException(Exception):
    code = 500


class ArgumentInvalid(ServerException):
    code = 400


class ArgumentRequired(ServerException):
    code = 403


class ObjectsDuplicated(ServerException):
    code = 403


class ObjectsNotExist(ServerException):
    code = 404


class PatternInvalid(ServerException):
    code = 403
