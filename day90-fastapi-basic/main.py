from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="Simple Note API", description="FastAPIによるREST APIの基本例", version="1.0.0")

# Pydanticモデル（リクエスト/レスポンス用）
class Note(BaseModel):
    id: int
    title: str
    content: str

# データストア（簡易的なメモリ上のDB）
notes: List[Note] = []

# 全てのノートを取得
@app.get("/notes", response_model=List[Note])
def get_notes():
    return notes

# IDでノートを取得
@app.get("/notes/{note_id}", response_model=Note)
def get_note(note_id: int):
    for note in notes:
        if note.id == note_id:
            return note
    raise HTTPException(status_code=404, detail="Note not found")

# ノートを作成
@app.post("/notes", response_model=Note)
def create_note(note: Note):
    if any(n.id == note.id for n in notes):
        raise HTTPException(status_code=400, detail="Note ID already exists")
    notes.append(note)
    return note

# ノートを更新
@app.put("/notes/{note_id}", response_model=Note)
def update_note(note_id: int, updated_note: Note):
    for index, note in enumerate(notes):
        if note.id == note_id:
            notes[index] = updated_note
            return updated_note
    raise HTTPException(status_code=404, detail="Note not found")

# ノートを削除
@app.delete("/notes/{note_id}")
def delete_note(note_id: int):
    for index, note in enumerate(notes):
        if note.id == note_id:
            notes.pop(index)
            return {"message": "Note deleted successfully"}
    raise HTTPException(status_code=404, detail="Note not found")
