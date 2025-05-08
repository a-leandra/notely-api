from datetime import datetime, timezone, tzinfo

from db import Base
from sqlalchemy import Text
from sqlalchemy.orm import Mapped, mapped_column


class Note(Base):
    """The dedicated database model for notes."""

    __tablename__ = "notes"

    id: Mapped[str] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    date_created: Mapped[datetime] = mapped_column(default=datetime.now)

    def __repr__(self):
        return f"<Note {self.title} at {self.date_created}>"
