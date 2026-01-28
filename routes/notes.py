from fastapi import APIRouter
from fastapi import Request
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")

from fastapi.responses import HTMLResponse, RedirectResponse

from models.note import Note
from config.db import conn
from schemas.note import Note as noteEntity, NoteList

note = APIRouter()

@note.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    docs = conn.notes.notes.find({})
    newDocs= []
    for doc in docs:
        newDocs.append(
            {
                "id": doc.get("_id"),
                "title": doc.get("title", "No Title"),
                "desc": doc.get("desc", "No Description")
            }
        )
    return templates.TemplateResponse("index.html", {"request": request, "docs": newDocs})

@note.post("/")
async def add_note(request: Request):
    form = await request.form()
    formData = dict(form)
    # Ensure title and desc exist, though .get() in read_item handles retrieval.
    conn.notes.notes.insert_one(formData)
    return RedirectResponse("/", status_code=303)