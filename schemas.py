from datetime import datetime

from pydantic import BaseModel, ConfigDict


class NoteModel(BaseModel):
    id: str
    title: str
    content: str
    date_created: datetime

    model_config = ConfigDict(
        from_attributes=True,
    )


class NoteCreateModel(BaseModel):
    title: str
    content: str

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {"title": "Example title", "content": "Example content"}
        },
    )
