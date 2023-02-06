"""Модуль роутера API v1."""
from fastapi import FastAPI

from src.api.v1 import admin
from src.api.v1 import events
from src.config.project import project_settings

router = FastAPI(**project_settings.dict())
router.include_router(events.router)
router.include_router(admin.router)
