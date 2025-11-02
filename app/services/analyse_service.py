# services/analyse_sol_service.py

from uuid import UUID
from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.analyse_sol import AnalyseSolCreate
from app.crud.analyse_sol import create_analyse_sol
from app.crud.parcelle import get_parcelle_by_id

async def creer_analyse_sol(db: AsyncSession, payload: AnalyseSolCreate):
    """
    Service métier pour créer une analyse de sol avec validation.
    """

    # Vérifier que la parcelle existe
    parcelle = await get_parcelle_by_id(db, payload.parcelle_id)
    if parcelle is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Parcelle introuvable"
        )


    # pH doit être entre 0 et 14
    if not (0 <= payload.ph <= 14):
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Le pH doit être compris entre 0 et 14."
        )

    # humidité entre 0% et 100%
    if not (0 <= payload.humidite <= 100):
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="L'humidité doit être comprise entre 0 et 100%."
        )

    # nutriments ne peuvent pas être négatifs
    if payload.n < 0 or payload.p < 0 or payload.k < 0:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Les valeurs N, P, K doivent être positives."
        )

    # Appel CRUD pour insertion
    analyse = await create_analyse_sol(db, payload)

    # Retourner le résultat
    return analyse
