import typing
from sqlalchemy import create_engine, Engine
from dashboard.core.config import Settings
from dashboard.db import dashboard
import structlog

LOGGER = structlog.get_logger()
LOGGER = LOGGER.bind(module=__name__)


class DatabaseClient:
    def __init__(self, engine: typing.Optional[Engine] = None):
        self._engine = engine or create_engine("sqlite://", echo=True)
        self._logger = LOGGER.bind(db_engine=self._engine.name)

    @property
    def engine(self) -> Engine:
        return self._engine

    def apply_schema(self, settings: Settings):
        self._logger.info("Applying database schema")
        dashboard.create_tables(self.engine, settings=settings)

    def seed(self, settings: Settings):
        self._logger.info("Seeding database")
        dashboard.seed_data(self.engine, settings)

    def bootstrap(self, settings: Settings):
        self.apply_schema(settings)
        self.seed(settings)

    async def shutdown(self):
        self._logger.info("Shutting down database")
        self.engine.dispose()
        self._logger.info("Database shutdown complete")
