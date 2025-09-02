import typing
from sqlalchemy import create_engine, Engine
from dashboard.core.config import Settings
from dashboard.db import dashboard
import structlog

LOGGER = structlog.get_logger()
LOGGER = LOGGER.bind(module=__name__)


class DatabaseClient:
    def __init__(self, settings: Settings, engine: typing.Optional[Engine] = None):
        self._engine = engine or create_engine(
            settings.connection_string,
            echo=True,
        )
        self._logger = LOGGER.bind(db_engine=self._engine.name)
        self.bootstrap(settings=settings)

    def __repr__(self):
        return (
            f"DatabaseClient(engine={self._engine.name}, host={self._engine.url.host})"
        )

    def __str__(self):
        return self.__repr__()

    @property
    def engine(self) -> Engine:
        return self._engine

    def apply_schema(self, settings: Settings):
        self._logger.info("Applying database schema")
        dashboard.create_tables(self.engine, settings=settings)

    def bootstrap(self, settings: Settings):
        self.apply_schema(settings)

    async def shutdown(self):
        self._logger.info("Shutting down database")
        self.engine.dispose()
        self._logger.info("Database shutdown complete")
