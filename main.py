import logging

import pkg_resources
from pathlib import Path

from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from backend import api, exception_handler, settings
from backend.config import configure_application
from backend.core.constants import ApplicationMode


logger = logging.getLogger(__name__)

configure_application()
app_settings = settings.get_settings()

fastapi_kwargs = {
    'title': 'Fast API Base',
    'description': 'Base FastAPI App',
    'version': pkg_resources.get_distribution("project-base").version,
}

if app_settings.APP_MODE not in [ApplicationMode.LOCAL, ApplicationMode.DEV]:
    fastapi_kwargs['docs_url'] = None
    fastapi_kwargs['redoc_url'] = None
    fastapi_kwargs['openapi_url'] = None

app = FastAPI(**fastapi_kwargs)

if app_settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in app_settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(api.router)

app.exception_handler(HTTPException)(exception_handler.http_exception_handler)
app.exception_handler(Exception)(exception_handler.unexpected_exception_handler)

fronted_build_path = Path(__file__).resolve().parent / "frontend" / "dist"

# TODO: rewrite to FastAPI docs
app.mount(
    "/js/",
    StaticFiles(directory=(fronted_build_path / 'js').as_posix()),
    name="Vue App js files",
)

app.mount(
    "/css/",
    StaticFiles(directory=(fronted_build_path / 'css').as_posix()),
    name="Vue App css files",
)

templates = Jinja2Templates(directory=fronted_build_path.as_posix())


@app.get("/{full_path:path}", include_in_schema=False)
async def proxy_app(request: Request, full_path: str):
    """Vue app proxy endpoint"""
    logger.debug(f"Proxy to Vue App, path: {full_path}")
    return templates.TemplateResponse("index.html", {"request": request})
