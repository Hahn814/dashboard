"""Load configuration from the environment"""


class Settings:
    def __init__(self):
        self._DEVELOPMENT = True

    @property
    def DEVELOPMENT(self):
        return self._DEVELOPMENT

    def __repr__(self):
        return f"Settings(DEVELOPMENT={self.DEVELOPMENT})"
