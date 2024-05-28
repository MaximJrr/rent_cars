from fastapi import HTTPException, status


class RentsException(HTTPException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    detail = ""

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class UserAlreadyExistsException(RentsException):
    status_code = status.HTTP_409_CONFLICT
    detail = "User already exists"


class UserNotExistsException(RentsException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "User not exists"


class PasswordNotCorrectException(RentsException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Password not correct"


class TokenNotExistsException(RentsException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Token not exists"


class InvalidTokenFormatException(RentsException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Invalid token format"


class ExpiredTokenException(RentsException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Expired token"


class CarCanNotBeRented(RentsException):
    status_code = status.HTTP_409_CONFLICT
    detail = "There are no free cars left"
