import os


class Config:
    OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]

    def get(name, default=None):
        return os.environ.get(name, default)


settings = Config()
