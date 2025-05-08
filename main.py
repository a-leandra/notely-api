import uuid
from http import HTTPStatus
from typing import List

from crud import CRUD
from db import engine
from fastapi import FastAPI
from models import Note
from schemas import NoteCreateModel, NoteModel
from sqlalchemy.ext.asyncio import async_sessionmaker

app = FastAPI(
    title="Notely API",
    description="A basic note-taking API which supports CRUD operations via a RESTful API for manipulating note objects.",
    docs_url="/",
)

# Create an async session object for the CRUD operations
session = async_sessionmaker(bind=engine, expire_on_commit=False)

db = CRUD()


@app.get("/notes", response_model=List[NoteModel])
async def get_all_notes():
    """API endpoint returning all of the available notes."""
    notes = await db.get_all(session)

    return notes


@app.post("/notes", status_code=HTTPStatus.CREATED)
async def create_note(note_data: NoteCreateModel):
    """API endpoint for creating a new note.

    Args:
        note_data (NoteCreateModel): Data for creating a note using the note schema.

    Returns:
        dict: Note that has just been created.
    """

    new_note = Note(
        id=str(uuid.uuid4()), title=note_data.title, content=note_data.content
    )

    note = await db.add(session, new_note)

    return note


@app.get("/note/{note_id}")
async def get_note_by_id(note_id):
    """API endpoint for retrieving a note by its ID.

    Args:
        note_id (str): The ID of the note to be retrieved.

    Returns:
        dict: The retrieved note.
    """

    note = await db.get_by_id(session, note_id)

    return note


@app.patch("/note/{note_id}")
async def update_note(note_id: str, data: NoteCreateModel):
    """Update a note by its ID.

    Args:
        note_id (str): ID of the note to updated.
        data (NoteCreateModel): Data to update the note.

    Returns:
        dict: The updated note.
    """

    note = await db.update(
        session, note_id, data={"title": data.title, "content": data.content}
    )

    return note


@app.delete("/note/{note_id}", status_code=HTTPStatus.NO_CONTENT)
async def delete_note(note_id: str):
    """Delete a note by its ID.

    Args:
        note_id (str): ID of the note to be deleted.

    """

    note = await db.get_by_id(session, note_id)

    result = await db.delete(session, note)
    return result
