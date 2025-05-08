import os

from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import DeclarativeBase

load_dotenv()

# Engine object to connect to the database
engine = create_async_engine(url=os.getenv("DATABASE_URL"), echo=True)


class Base(DeclarativeBase):
    """Base class for creating database models"""

    pass
