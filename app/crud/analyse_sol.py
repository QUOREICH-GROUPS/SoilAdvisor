from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database.base import SessionLocal
from app.models.analyse_sol import AnalyseSol
from app.models.parcelle import Parcelle
from app.schemas.analyse_sol import AnalyseSolCreate, AnalyseSolResponse
router = APIRouter()
import app
# Dépendance pour obtenir la session de base de données
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close() 

# ENDPOINTS ANALYSES SOL
@app.post("/analyses-sol", response_model=AnalyseSolResponse)
def creer_analyse_sol(analyse: AnalyseSolCreate, db: Session = Depends(get_db)):
    db_parcelle = db.query(Parcelle).filter(Parcelle.id == analyse.parcelle_id).first()
    if not db_parcelle:
        raise HTTPException(status_code=404, detail="Parcelle non trouvée")
    db_analyse = AnalyseSol(**analyse.dict())
    db.add(db_analyse)
    db.commit()
    db.refresh(db_analyse)
    return db_analyse

@app.get("/analyses-sol/parcelle/{parcelle_id}", response_model=List[AnalyseSolResponse])
def lister_analyses_parcelle(parcelle_id: int, db: Session = Depends(get_db)):
    return db.query(AnalyseSol).filter(AnalyseSol.parcelle_id == parcelle_id).all()

@app.get("/analyses-sol/{analyse_id}", response_model=AnalyseSolResponse)
def obtenir_analyse(analyse_id: int, db: Session = Depends(get_db)):
    db_analyse = db.query(AnalyseSol).filter(AnalyseSol.id == analyse_id).first()
    if not db_analyse:
        raise HTTPException(status_code=404, detail="Analyse non trouvée")
    return db_analyse

@app.delete("/analyses-sol/{analyse_id}")
def supprimer_analyse(analyse_id: int, db: Session = Depends(get_db)):
    db_analyse = db.query(AnalyseSol).filter(AnalyseSol.id == analyse_id).first()
    if not db_analyse:
        raise HTTPException(status_code=404, detail="Analyse non trouvée")
    db.delete(db_analyse)
    db.commit()
    return {"message": "Analyse supprimée"}