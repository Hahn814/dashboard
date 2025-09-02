"""Load configuration from the environment"""

import os


class Settings:
    def __init__(self):
        self._DEVELOPMENT = os.getenv("DEVELOPMENT", "False").lower() in (
            "true",
            "1",
            "t",
        )

        self._db_user = os.getenv("POSTGRES_USER", None)
        if not self._db_user:
            raise ValueError("POSTGRES_USER environment variable is required")

        self._db_password = os.getenv("POSTGRES_PASSWORD", None)
        if not self._db_password:
            raise ValueError("POSTGRES_PASSWORD environment variable is required")

        self._db_host = os.getenv("POSTGRES_HOST", None)
        if not self._db_host:
            raise ValueError("POSTGRES_HOST environment variable is required")

        self._db_name = os.getenv("POSTGRES_DB", None)
        if not self._db_name:
            raise ValueError("POSTGRES_DB environment variable is required")

    @property
    def DEVELOPMENT(self):
        return self._DEVELOPMENT

    @property
    def connection_string(self):
        return f"postgresql+psycopg2://{self._db_user}:{self._db_password}@{self._db_host}/{self._db_name}"

    def __repr__(self):
        return f"Settings(DEVELOPMENT={self.DEVELOPMENT})"
