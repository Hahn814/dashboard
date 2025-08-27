from fastapi import FastAPI
from dashboard.api.v1.endpoints import task
from dashboard.api.query import router as query_router
from dashboard.core.config import Settings
from dashboard.db import DatabaseClient
from contextlib import asynccontextmanager
import structlog

LOGGER = structlog.get_logger()
LOGGER = LOGGER.bind(module=__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.settings = Settings()
    LOGGER.info("Settings initialized", settings=app.state.settings)

    client = DatabaseClient()
    client.bootstrap(app.state.settings)
    app.state.db = client
    LOGGER.debug("Database client initialized", client=client)

    yield
    await client.shutdown()


app = FastAPI(lifespan=lifespan)
app.include_router(task.router)
app.include_router(query_router, prefix="/graphql")


@app.get("/")
def read_root():
    return {"message": "Welcome to the Dashboard API"}
