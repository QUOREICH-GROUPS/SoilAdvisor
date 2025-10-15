from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import app
from app.database.base import SessionLocal
from app.models.parcelle import Parcelle
from app.schemas.parcelle import ParcelleCreate, ParcelleResponse
router = APIRouter()
# Dépendance pour obtenir la session de base de données
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
        
# ENDPOINTS PARCELLES
@app.post("/parcelles", response_model=ParcelleResponse)
def creer_parcelle(parcelle: ParcelleCreate, db: Session = Depends(get_db)):
    db_parcelle = Parcelle(**parcelle.dict())
    db.add(db_parcelle)
    db.commit()
    db.refresh(db_parcelle)
    return db_parcelle

@app.get("/parcelles", response_model=List[ParcelleResponse])
def lister_parcelles(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(Parcelle).offset(skip).limit(limit).all()

@app.get("/parcelles/{parcelle_id}", response_model=ParcelleResponse)
def obtenir_parcelle(parcelle_id: int, db: Session = Depends(get_db)):
    db_parcelle = db.query(Parcelle).filter(Parcelle.id == parcelle_id).first()
    if not db_parcelle:
        raise HTTPException(status_code=404, detail="Parcelle non trouvée")
    return db_parcelle

@app.put("/parcelles/{parcelle_id}", response_model=ParcelleResponse)
def mettre_a_jour_parcelle(parcelle_id: int, parcelle: ParcelleCreate, db: Session = Depends(get_db)):
    db_parcelle = db.query(Parcelle).filter(Parcelle.id == parcelle_id).first()
    if not db_parcelle:
        raise HTTPException(status_code=404, detail="Parcelle non trouvée")
    for key, value in parcelle.dict().items():
        setattr(db_parcelle, key, value)
    db.commit()
    db.refresh(db_parcelle)
    return db_parcelle

@app.delete("/parcelles/{parcelle_id}")
def supprimer_parcelle(parcelle_id: int, db: Session = Depends(get_db)):
    db_parcelle = db.query(Parcelle).filter(Parcelle.id == parcelle_id).first()
    if not db_parcelle:
        raise HTTPException(status_code=404, detail="Parcelle non trouvée")
    db.delete(db_parcelle)
    db.commit()
    return {"message": "Parcelle supprimée"}