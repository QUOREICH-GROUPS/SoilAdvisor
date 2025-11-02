from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.session import SessionLocal


def get_db() -> Session:
    """Dépendance pour obtenir une session de base de données"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()