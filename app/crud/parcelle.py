from typing import List
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.session import get_db
from app.schemas.parcelle import ParcelleCreate, ParcelleResponse
from app.services.parcelle_service import (
    creer_parcelle,
    lister_parcelles_service,
    obtenir_parcelle_service,
    mettre_a_jour_parcelle_service,
    supprimer_parcelle_service
)
 # AsyncSession

router = APIRouter(prefix="/api/v1/parcelles", tags=["Parcelles"])

# -------------------------------
# Lister les parcelles
# -------------------------------
@router.get("/", response_model=List[ParcelleResponse])
async def lister_parcelles(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)):
    return await lister_parcelles_service(db, skip, limit)

# -------------------------------
# Obtenir une parcelle par ID
# -------------------------------
@router.get("/{parcelle_id}", response_model=ParcelleResponse)
async def obtenir_parcelle(parcelle_id: UUID, db: AsyncSession = Depends(get_db)):
    parcelle = await obtenir_parcelle_service(db, parcelle_id)
    if not parcelle:
        raise HTTPException(status_code=404, detail="Parcelle non trouvée")
    return parcelle

# -------------------------------
# Créer une parcelle
# -------------------------------
@router.post("/", response_model=ParcelleResponse)
async def creer_parcelle_endpoint(parcelle: ParcelleCreate, db: AsyncSession = Depends(get_db)):
    return await creer_parcelle(db, parcelle)

# -------------------------------
# Mettre à jour une parcelle
# -------------------------------
@router.put("/{parcelle_id}", response_model=ParcelleResponse)
async def mettre_a_jour_parcelle(parcelle_id: UUID, parcelle: ParcelleCreate, db: AsyncSession = Depends(get_db)):
    return await mettre_a_jour_parcelle_service(db, parcelle_id, parcelle)

# -------------------------------
# Supprimer une parcelle
# -------------------------------
@router.delete("/{parcelle_id}")
async def supprimer_parcelle(parcelle_id: UUID, db: AsyncSession = Depends(get_db)):
    return await supprimer_parcelle_service(db, parcelle_id)
