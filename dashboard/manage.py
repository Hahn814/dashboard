import sys
import os

# add project root to sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

import argparse
import structlog
from sqlalchemy.orm import Session


from dashboard.core.config import Settings
from dashboard.db import DatabaseClient
from dashboard.models.task import Task

LOGGER = structlog.get_logger()
LOGGER = LOGGER.bind(module=__name__)


def get_arg_parser():
    parser = argparse.ArgumentParser(description="Dashboard Management")
    subparsers = parser.add_subparsers(dest="command")
    seed_parser = subparsers.add_parser(
        "seed", help="Seed the database with sample tasks"
    )
    seed_parser.add_argument(
        "--clear", action="store_true", help="Clear existing data before seeding"
    )

    return parser


client = DatabaseClient(settings=Settings())
client.bootstrap(settings=Settings())

args = get_arg_parser().parse_args()
LOGGER.info(f"Parsed arguments: {args}")

if args.command == "seed":
    print("Seeding the database...")
    tasks = [
        Task(name="Sample Task #1", pk=1),
        Task(name="Sample Task #2", pk=2),
        Task(name="Sample Task #3", pk=3),
    ]

    with Session(client.engine) as session:
        if args.clear:
            Task.__table__.drop(client.engine)
            Task.__table__.create(client.engine)

        for task in tasks:
            existing_task = Task.get_task(task.pk, session)
            if existing_task:
                LOGGER.debug(f"Task with pk={task.pk} already exists. Skipping.")
                continue

            session.add(task)
            session.commit()

    LOGGER.info("Database seeded successfully.")
