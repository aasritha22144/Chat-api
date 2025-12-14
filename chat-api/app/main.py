from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel

from .database import SessionLocal, engine, Base
from .models import Message

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Chat History API")

# DB dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --------- Schemas ---------

class MessageCreate(BaseModel):
    user: Optional[str] = None
    message: Optional[str] = None

class MessageResponse(BaseModel):
    id: int
    user: str
    message: str
    timestamp: datetime

    class Config:
        orm_mode = True

# --------- Routes ---------

# POST /messages
@app.post("/messages", status_code=201)
def create_message(data: MessageCreate, db: Session = Depends(get_db)):
    if not data.user or not data.message:
        raise HTTPException(status_code=400, detail="User and message required")

    msg = Message(user=data.user, message=data.message)
    db.add(msg)
    db.commit()
    db.refresh(msg)

    return {"id": msg.id, "status": "saved"}

# GET /messages
@app.get("/messages", response_model=List[MessageResponse])
def get_messages(db: Session = Depends(get_db)):
    return db.query(Message).order_by(Message.timestamp).all()

# GET /messages/{user}
@app.get("/messages/{user}", response_model=List[MessageResponse])
def get_messages_by_user(user: str, db: Session = Depends(get_db)):
    return db.query(Message).filter(Message.user == user).all()

# DELETE /messages
@app.delete("/messages")
def clear_messages(db: Session = Depends(get_db)):
    db.query(Message).delete()
    db.commit()
    return {"status": "cleared"}
