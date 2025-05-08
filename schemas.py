from datetime import datetime

from pydantic import BaseModel, ConfigDict


class NoteModel(BaseModel):
    """Schema for retrieving a note."""

    id: str
    title: str
    content: str
    date_created: datetime

    model_config = ConfigDict(
        from_attributes=True,
    )


class NoteCreateModel(BaseModel):
    """Schema for creating/updating a note."""

    title: str
    content: str

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {"title": "Example title", "content": "Example content"}
        },
    )
