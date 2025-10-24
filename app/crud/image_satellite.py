from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from app.database.base import SessionLocal
from app.models.image_satellite import ImageSatellite
from app.models.parcelle import Parcelle
from app.schemas.image_satellite import ImageSatelliteCreate, ImageSatelliteResponse
app = FastAPI()
import app
# Dépendance pour obtenir la session de base de données
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ENDPOINTS IMAGES SATELLITE
@app.post("/images-satellite", response_model=ImageSatelliteResponse)
def creer_image_satellite(image: ImageSatelliteCreate, db: Session = Depends(get_db)):
    db_parcelle = db.query(Parcelle).filter(Parcelle.id == image.parcelle_id).first()
    if not db_parcelle:
        raise HTTPException(status_code=404, detail="Parcelle non trouvée")
    db_image = ImageSatellite(**image.dict())
    db.add(db_image)
    db.commit()
    db.refresh(db_image)
    return db_image

@app.get("/images-satellite/parcelle/{parcelle_id}", response_model=List[ImageSatelliteResponse])
def lister_images_parcelle(parcelle_id: int, db: Session = Depends(get_db)):
    return db.query(ImageSatellite).filter(ImageSatellite.parcelle_id == parcelle_id).all()

@app.get("/images-satellite/{image_id}", response_model=ImageSatelliteResponse)
def obtenir_image(image_id: int, db: Session = Depends(get_db)):
    db_image = db.query(ImageSatellite).filter(ImageSatellite.id == image_id).first()
    if not db_image:
        raise HTTPException(status_code=404, detail="Image non trouvée")
    return db_image

@app.delete("/images-satellite/{image_id}")
def supprimer_image(image_id: int, db: Session = Depends(get_db)):
    db_image = db.query(ImageSatellite).filter(ImageSatellite.id == image_id).first()
    if not db_image:
        raise HTTPException(status_code=404, detail="Image non trouvée")
    db.delete(db_image)
    db.commit()
    return {"message": "Image supprimée"}

# ENDPOINT DE SANTÉ
@app.get("/health")
def health_check():
    return {"status": "API en bonne santé"}