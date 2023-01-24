from fastapi import APIRouter

from backend.config import configure_application
configure_application()

from backend.api import v1  # noqa E402


router = APIRouter(
    prefix="/api"
)

router.include_router(v1.router)
