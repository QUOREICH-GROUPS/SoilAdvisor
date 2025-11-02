# services/parcelle_service.py

from typing import List
from uuid import UUID
from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.models.parcelle import Parcelle
from app.schemas.parcelle import ParcelleCreate, ParcelleResponse

# -------------------------------
# Créer une parcelle
# -------------------------------
async def creer_parcelle(db: AsyncSession, parcelle: ParcelleCreate) -> ParcelleResponse:
    new_parcelle = Parcelle(
        nom=parcelle.nom,
        geom=parcelle.geom,
        #proprietaire_id=parcelle.proprietaire_id,
        surface_ha=parcelle.surface_ha
    )
    db.add(new_parcelle)
    await db.commit()
    await db.refresh(new_parcelle)
    return ParcelleResponse.model_validate(new_parcelle)

# -------------------------------
# Lister les parcelles
# -------------------------------
async def lister_parcelles_service(db: AsyncSession, skip: int = 0, limit: int = 10) -> List[ParcelleResponse]:
    result = await db.execute(select(Parcelle).offset(skip).limit(limit))
    parcelles = result.scalars().all()
    return [ParcelleResponse.model_validate(p) for p in parcelles]

# -------------------------------
# Obtenir une parcelle par ID
# -------------------------------
async def obtenir_parcelle_service(db: AsyncSession, parcelle_id: UUID) -> ParcelleResponse | None:
    result = await db.execute(select(Parcelle).where(Parcelle.id == parcelle_id))
    parcelle = result.scalar_one_or_none()
    return ParcelleResponse.model_validate(parcelle) if parcelle else None

# -------------------------------
# Mettre à jour une parcelle
# -------------------------------
async def mettre_a_jour_parcelle_service(db: AsyncSession, parcelle_id: UUID, parcelle_update: ParcelleCreate) -> ParcelleResponse:
    result = await db.execute(select(Parcelle).where(Parcelle.id == parcelle_id))
    parcelle = result.scalar_one_or_none()
    if not parcelle:
        raise HTTPException(status_code=404, detail="Parcelle non trouvée")

    for key, value in parcelle_update.dict().items():
        setattr(parcelle, key, value)

    await db.commit()
    await db.refresh(parcelle)
    return ParcelleResponse.model_validate(parcelle)

# -------------------------------
# Supprimer une parcelle
# -------------------------------
async def supprimer_parcelle_service(db: AsyncSession, parcelle_id: UUID) -> dict:
    result = await db.execute(select(Parcelle).where(Parcelle.id == parcelle_id))
    parcelle = result.scalar_one_or_none()
    if not parcelle:
        raise HTTPException(status_code=404, detail="Parcelle non trouvée")

    await db.delete(parcelle)
    await db.commit()
    return {"message": "Parcelle supprimée"}
