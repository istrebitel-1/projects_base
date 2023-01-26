from pydantic import BaseModel

from backend.api.v1.common_endpoints import constants
from backend.core.models import APIResponse


class AppModePayload(BaseModel):
    """App mode model"""
    mode: str


class AppVersionPayload(BaseModel):
    """App version model"""
    version: str


class AppModeAPIResponse(APIResponse):
    """App mode API response"""
    message: str = constants.APIResponseMessageTemplate.BACKEND_MODE_INFO
    payload: AppModePayload


class AppVersionAPIResponse(APIResponse):
    """App version API response"""
    message: str = constants.APIResponseMessageTemplate.VERSION_INFO
    payload: AppVersionPayload


class AppConfigAPIResponse(APIResponse):
    """App config API response"""
    message: str = constants.APIResponseMessageTemplate.CONFIGURATION_INFO
    payload: dict
