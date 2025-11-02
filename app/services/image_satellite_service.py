# services/image_satellite_service.py

from datetime import datetime
from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID

from app.schemas.image_satellite import ImageSatelliteCreate, ImageSatelliteResponse
from app.crud.image_satellite import create_image_satellite
from app.crud.parcelle import get_parcelle_by_id


async def ajouter_image_satellite(
    db: AsyncSession,
    payload: ImageSatelliteCreate
) -> ImageSatelliteResponse:
    """
    Service métier pour créer une image satellite associée à une parcelle.
    Validation :
    - parcelle existante
    - captured_at pas dans le futur
    - URL et satellite_id valides (si fournis)
    """

    # 1️⃣ Vérifier que la parcelle existe
    parcelle = await get_parcelle_by_id(db, UUID(payload.satellite_id)) if payload.satellite_id else None
    if payload.satellite_id and parcelle is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Parcelle introuvable pour le satellite fourni"
        )

    # 2️⃣ Vérifier que la date de capture n'est pas dans le futur
    if payload.captured_at and payload.captured_at > datetime.utcnow():
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="La date de capture ne peut pas être dans le futur"
        )

    # 3️⃣ Optionnel : vérification URL et satellite_id (syntaxe)
    if payload.url:
        if not payload.url.startswith("http"):
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail="L'URL doit commencer par http:// ou https://"
            )

    # 4️⃣ Création via CRUD
    image = await create_image_satellite(db, payload)

    # 5️⃣ Retourner le schéma de réponse
    return image
