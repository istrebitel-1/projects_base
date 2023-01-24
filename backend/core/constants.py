from enum import Enum


class AppStringEnum(str, Enum):
    """Base Enum class for strings"""
    def __str__(self):
        return self.value


class AppNumberEnum(int, Enum):
    """Base Enum class for int's"""
    def __str__(self):
        return str(self.value)


class APIResponseStatus(AppStringEnum):
    """API Response statuses"""
    ERROR = 'error'
    SUCCESS = 'success'


class ApplicationMode(AppStringEnum):
    """App work modes"""
    LOCAL = 'LOCAL'
    DEV = 'DEV'
    UAT = 'UAT'
    PROD = 'PROD'


class UserRole(AppStringEnum):
    """Base user roles"""
    ADMIN = 'ADMIN'
    USER = 'USER'
    VIEWER = 'VIEWER'


class HTTPCodesMessage(AppStringEnum):
    """HTTP codes messages"""
    HTTP_200_OK = 'Successful response'
    HTTP_307_TEMPORARY_REDIRECT = 'Temporary Redirect'
    HTTP_400_BAD_REQUEST = 'Bad request'
    HTTP_401_UNAUTHORIZED = 'Unauthorized'
    HTTP_403_FORBIDDEN = 'Forbidden'
    HTTP_404_NOT_FOUND = 'Not found'
    HTTP_503_SERVICE_UNAVAILABLE = 'Service Unavailable'


class ErrorResponseMessageTemplate(AppStringEnum):
    """Common exception messages"""
    CORRECTION_DATA_NULL_VALUE_ERROR = 'Some field violates not null constraint'
    CORRECTION_DATA_TYPE_ERROR = 'Incorrect data type'
    DATABASE_COMMON_ERROR = 'Database error'
    DATABASE_CONNECTION_ERROR = 'Database connection can not be established'
