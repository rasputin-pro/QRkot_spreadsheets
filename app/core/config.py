import logging
import sys
from typing import Optional

from pydantic import BaseSettings, EmailStr


class Settings(BaseSettings):
    app_title: str = 'Кошачий благотворительный фонд (0.1.0)'
    description: str = 'Сервис для поддержки котиков!'
    database_url: str = 'sqlite+aiosqlite:///./fastapi.db'
    secret: str = 'SECRET'
    first_superuser_email: Optional[EmailStr] = None
    first_superuser_password: Optional[str] = None

    class Config:
        env_file = '.env'


settings = Settings()

logging.basicConfig(
    level=logging.INFO,
    stream=sys.stdout,
    format=('%(asctime)s | %(levelname)s | %(message)s '
            '| %(filename)s:%(lineno)d '),
)
