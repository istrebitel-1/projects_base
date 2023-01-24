from typing import Union, List, Dict

from fastapi import status as fastapi_status
from pydantic import BaseModel

from backend.core.constants import APIResponseStatus


class APIResponse(BaseModel):
    """Base API response"""
    status: str = APIResponseStatus.SUCCESS
    status_code: int = fastapi_status.HTTP_200_OK
    message: str = None
    payload: Union[BaseModel, List, Dict] = None


class ErrorAPIResponse(APIResponse):
    """Error API response"""
    status = APIResponseStatus.ERROR
