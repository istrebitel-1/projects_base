from fastapi import APIRouter

from backend.api.v1.common_endpoints.routes import router as info_router


router = APIRouter(
    prefix="/v1"
)

router.include_router(info_router)
