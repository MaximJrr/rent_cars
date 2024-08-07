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


class CarCanNotBeRentedException(RentsException):
    status_code = status.HTTP_409_CONFLICT
    detail = "There are no free cars left"


class NoCarException(RentsException):
    status_code = status.HTTP_409_CONFLICT
    detail = "No car"


class UserNotFoundException(RentsException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = "User not found"


class NotAuthorizedToUpdateThisUser(RentsException):
    status_code = status.HTTP_403_FORBIDDEN
    detail = "Not authorized to update this user"


class NoRentException(RentsException):
    status_code = status.HTTP_409_CONFLICT
    detail = "No rent"
