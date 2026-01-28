def Note(item) -> dict:
    return {"id": str(item["_id"]),
     "title": item["title"],
     "desc": item["desc"]
     }


def NoteList(items) -> list:
    return [Note(item) for item in items]
