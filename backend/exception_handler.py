import logging

import psycopg2
from fastapi import status, HTTPException
from fastapi.responses import JSONResponse

from backend.core import models
from backend.core.constants import ErrorResponseMessageTemplate
from backend.core.utils import make_response


logger = logging.getLogger(__name__)


def http_exception_handler(request, exc: HTTPException) -> JSONResponse:
    """HTTPException handler"""
    http_exception_response = models.ErrorAPIResponse(
        status_code=exc.status_code,
        message=exc.detail
    )

    logger.error(f'An HTTPException was thrown while processing a request along the path {request.scope.get("path")}:'
                 f' status_code={exc.status_code}, message={exc.detail}')

    return make_response(api_response=http_exception_response)


def unexpected_exception_handler(request, exc: Exception) -> JSONResponse:
    """Unexpected error handler"""
    unexpected_exception_response = _get_error_response_for_exception(exc=exc)

    logger.error(f'Error in request processing logic {request.scope.get("path")}: {_get_exception_message(exc=exc)}')

    return make_response(api_response=unexpected_exception_response)


def _get_exception_message(exc: Exception) -> str:
    """Get an Error, based on an Exception"""
    return f'{exc.__class__.__name__}: {str(exc)}'


def _get_error_response_for_exception(exc: Exception) -> models.ErrorAPIResponse:
    """Get an Error, based on an specific Exception"""
    common_exceptions = [
        {
            'class': psycopg2.errors.ConnectionException,  # noqa
            'status_code': status.HTTP_500_INTERNAL_SERVER_ERROR,
            'message': ErrorResponseMessageTemplate.DATABASE_CONNECTION_ERROR,
        },
        {
            'class': psycopg2.errors.InvalidTextRepresentation,  # noqa
            'status_code': status.HTTP_400_BAD_REQUEST,
            'message': ErrorResponseMessageTemplate.CORRECTION_DATA_TYPE_ERROR,
        },
        {
            'class': psycopg2.errors.NotNullViolation,  # noqa
            'status_code': status.HTTP_400_BAD_REQUEST,
            'message': ErrorResponseMessageTemplate.CORRECTION_DATA_NULL_VALUE_ERROR,
        },
        {
            'class': psycopg2.errors.DatabaseError,  # noqa
            'status_code': status.HTTP_500_INTERNAL_SERVER_ERROR,
            'message': ErrorResponseMessageTemplate.DATABASE_COMMON_ERROR,
        },
    ]

    for exception in common_exceptions:
        if isinstance(exc, exception['class']):
            return models.ErrorAPIResponse(
                status_code=exception['status_code'],
                message=exception['message'],
            )

    return models.ErrorAPIResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        message=_get_exception_message(exc=exc),
    )
