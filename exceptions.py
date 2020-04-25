from werkzeug.exceptions import HTTPException


class ServerException(Exception):
    code = 500
