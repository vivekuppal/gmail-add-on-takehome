import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI
from .routes import router
from .settings import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    logging.basicConfig(level=getattr(logging, settings.log_level.upper(), logging.INFO))
    logging.getLogger(__name__).info("Starting %s (%s)", settings.app_name, settings.environment)

    # If you later add DB/clients, init them here and attach to app.state

    yield

    logging.getLogger(__name__).info("Shutting down %s", settings.app_name)


app = FastAPI(title=settings.app_name, lifespan=lifespan)
app.include_router(router)
