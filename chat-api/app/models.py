from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from .database import Base

class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    user = Column(String, nullable=False, index=True)
    message = Column(String, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)
