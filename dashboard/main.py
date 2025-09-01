from fastapi import FastAPI
from dashboard.api.v1.endpoints import task
from dashboard.api.query import router as query_router
from dashboard.core.config import Settings
from dashboard.db import DatabaseClient
from contextlib import asynccontextmanager
import structlog

LOGGER = structlog.get_logger()
LOGGER = LOGGER.bind(module=__name__)

client = DatabaseClient(Settings())


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.settings = Settings()
    LOGGER.info("Settings attached to FastAPI", settings=app.state.settings)

    app.state.db = client
    LOGGER.debug("Database client attached to FastAPI", client=client)

    yield
    await client.shutdown()


app = FastAPI(lifespan=lifespan)
app.include_router(task.router)
app.include_router(query_router, prefix="/graphql")


@app.get("/")
def read_root():
    return {"message": "Welcome to the Dashboard API"}
