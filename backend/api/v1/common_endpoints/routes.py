import logging

from fastapi import APIRouter, Depends

from backend.api.v1.common_endpoints import models
from backend.core.utils import make_response
from backend.settings import get_settings, Settings


logger = logging.getLogger(__name__)

router = APIRouter(
    prefix='/info',
    tags=['info'],
)


@router.get(
    "/mode",
    response_model=models.AppModeAPIResponse,
    name="info_get_app_mode",
)
def get_app_mode(settings: Settings = Depends(get_settings)):
    """Get App work mode"""
    return make_response(
        api_response=models.AppModeAPIResponse(
            payload=models.AppModePayload(mode=settings.APP_MODE),
        )
    )


@router.get(
    "/version",
    response_model=models.AppVersionAPIResponse,
    name="info_get_app_version",
)
def get_app_version(settings: Settings = Depends(get_settings)):
    """Get app version"""
    return make_response(
        api_response=models.AppVersionAPIResponse(
            payload=models.AppVersionPayload(version=settings.APP_VERSION),
        )
    )


@router.get(
    "/configuration",
    response_model=models.AppConfigAPIResponse,
    name="info_get_app_configuration",
)
def get_app_configuration(settings: Settings = Depends(get_settings)):
    """Get insensitive App's config information"""
    payload = settings.get_insensitive_configuration()

    return make_response(
        api_response=models.AppConfigAPIResponse(
            payload=payload,
        )
    )
