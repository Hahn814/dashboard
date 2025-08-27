from dashboard.core.config import Settings
from dashboard.models.task import Base as TaskBase
import structlog

LOGGER = structlog.get_logger()
LOGGER = LOGGER.bind(module=__name__)


def seed_data(engine, settings: Settings):
    if settings.DEVELOPMENT:
        # TODO: Seed the database with initial data
        pass


def create_tables(engine, settings: Settings):
    LOGGER.info("Creating tables in the database")
    TaskBase.metadata.create_all(bind=engine)
