import os
from dotenv import load_dotenv

load_dotenv()


class Settings:

    origins = [
        "http://localhost:5173"
    ]

    SECRET_KEY = os.getenv(
        "SECRET_KEY",
        "mysecretkey123"
    )

    DB_URL = os.getenv(
        "DB_URL",
        "sqlite:///./test.db"
    )


settings = Settings()