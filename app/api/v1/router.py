from fastapi import APIRouter, Depends, File, HTTPException, UploadFile, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import UUID, select
from typing import List

from app.crud.recommandation import RecommendationEngine, Region
from app.crud.upload_file import create_upload, get_all_uploads
from app.database.session import get_db
from app.models.parcelle import Parcelle
from app.models.image_satellite import ImageSatellite
from app.models.analyse_sol import AnalyseSol

from app.models.recommandation import Recommandation
from app.schemas.parcelle import ParcelleCreate, ParcelleResponse
from app.schemas.image_satellite import ImageSatelliteCreate, ImageSatelliteResponse
from app.schemas.analyse_sol import AnalyseSolCreate, AnalyseSolResponse
from app.schemas.recommandation import AnalyseSolInfo, CultureRecommendation, RecommendationRequest, RecommendationResponse
from app.schemas.upload_file import UploadResponse
from app.services.upload_file_service import save_uploaded_file


router = APIRouter()

# ===========================
# Parcelles
# ===========================

@router.get("/parcelles", response_model=List[ParcelleResponse], tags=["Parcelles"])
async def list_parcelles(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Parcelle))
    return result.scalars().all()

@router.get("/parcelles/{parcelle_id}", response_model=ParcelleResponse, tags=["Parcelles"])
async def get_parcelle(parcelle_id: int, db: AsyncSession = Depends(get_db)):
    parcelle = await db.get(Parcelle, parcelle_id)
    if not parcelle:
        raise HTTPException(status_code=404, detail="Parcelle non trouvée")
    return parcelle

@router.post("/parcelles", response_model=ParcelleResponse, tags=["Parcelles"])
async def create_parcelle(payload: ParcelleCreate, db: AsyncSession = Depends(get_db)):
    db_parcelle = Parcelle(**payload.model_dump())
    db.add(db_parcelle)
    await db.commit()
    await db.refresh(db_parcelle)
    return db_parcelle

@router.put("/parcelles/{parcelle_id}", response_model=ParcelleResponse, tags=["Parcelles"])
async def update_parcelle(parcelle_id: int, payload: ParcelleCreate, db: AsyncSession = Depends(get_db)):
    parcelle = await db.get(Parcelle, parcelle_id)
    if not parcelle:
        raise HTTPException(status_code=404, detail="Parcelle non trouvée")
    for key, value in payload.model_dump().items():
        setattr(parcelle, key, value)
    await db.commit()
    await db.refresh(parcelle)
    return parcelle

@router.delete("/parcelles/{parcelle_id}", tags=["Parcelles"])
async def delete_parcelle(parcelle_id: int, db: AsyncSession = Depends(get_db)):
    parcelle = await db.get(Parcelle, parcelle_id)
    if not parcelle:
        raise HTTPException(status_code=404, detail="Parcelle non trouvée")
    await db.delete(parcelle)
    await db.commit()
    return {"message": f"Parcelle {parcelle_id} supprimée"}

# ===========================
# Images Satellite
# ===========================

@router.get("/images-satellite", response_model=List[ImageSatelliteResponse], tags=["Images-satellite"])
async def list_images(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(ImageSatellite))
    return result.scalars().all()

@router.get("/images-satellite/{image_id}", response_model=ImageSatelliteResponse, tags=["Images-satellite"])
async def get_image(image_id: int, db: AsyncSession = Depends(get_db)):
    image = await db.get(ImageSatellite, image_id)
    if not image:
        raise HTTPException(status_code=404, detail="Image satellite non trouvée")
    return image

@router.post("/images-satellite", response_model=ImageSatelliteResponse, tags=["Images-satellite"])
async def create_image(payload: ImageSatelliteCreate, db: AsyncSession = Depends(get_db)):
    db_image = ImageSatellite(**payload.model_dump())
    db.add(db_image)
    await db.commit()
    await db.refresh(db_image)
    return db_image

@router.put("/images-satellite/{image_id}", response_model=ImageSatelliteResponse, tags=["Images-satellite"])
async def update_image(image_id: int, payload: ImageSatelliteCreate, db: AsyncSession = Depends(get_db)):
    image = await db.get(ImageSatellite, image_id)
    if not image:
        raise HTTPException(status_code=404, detail="Image satellite non trouvée")
    for key, value in payload.model_dump().items():
        setattr(image, key, value)
    await db.commit()
    await db.refresh(image)
    return image

@router.delete("/images-satellite/{image_id}", tags=["Images-satellite"])
async def delete_image(image_id: int, db: AsyncSession = Depends(get_db)):
    image = await db.get(ImageSatellite, image_id)
    if not image:
        raise HTTPException(status_code=404, detail="Image satellite non trouvée")
    await db.delete(image)
    await db.commit()
    return {"message": f"Image satellite {image_id} supprimée"}

# ===========================
# Analyses de sol
# ===========================

@router.get("/analyses-sol", response_model=List[AnalyseSolResponse], tags=["Analyses-sol"])
async def list_analyses(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(AnalyseSol))
    return result.scalars().all()

@router.get("/analyses-sol/{analysis_id}", response_model=AnalyseSolResponse, tags=["Analyses-sol"])
async def get_analysis(analysis_id: int, db: AsyncSession = Depends(get_db)):
    analysis = await db.get(AnalyseSol, analysis_id)
    if not analysis:
        raise HTTPException(status_code=404, detail="Analyse de sol non trouvée")
    return analysis

@router.post("/analyses-sol", response_model=AnalyseSolResponse, tags=["Analyses-sol"])
async def create_analysis(payload: AnalyseSolCreate, db: AsyncSession = Depends(get_db)):
    db_analysis = AnalyseSol(**payload.model_dump())
    db.add(db_analysis)
    await db.commit()
    await db.refresh(db_analysis)
    return db_analysis

@router.put("/analyses-sol/{analysis_id}", response_model=AnalyseSolResponse, tags=["Analyses-sol"])
async def update_analysis(analysis_id: int, payload: AnalyseSolCreate, db: AsyncSession = Depends(get_db)):
    analysis = await db.get(AnalyseSol, analysis_id)
    if not analysis:
        raise HTTPException(status_code=404, detail="Analyse de sol non trouvée")
    for key, value in payload.model_dump().items():
        setattr(analysis, key, value)
    await db.commit()
    await db.refresh(analysis)
    return analysis

@router.delete("/analyses-sol/{analysis_id}", tags=["Analyses-sol"])
async def delete_analysis(analysis_id: int, db: AsyncSession = Depends(get_db)):
    analysis = await db.get(AnalyseSol, analysis_id)
    if not analysis:
        raise HTTPException(status_code=404, detail="Analyse de sol non trouvée")
    await db.delete(analysis)
    await db.commit()
    return {"message": f"Analyse de sol {analysis_id} supprimée"}
# ===========================
# Fichiers
# ===========================
@router.post("/fichier", response_model=List[UploadResponse],tags=["Fichiers"])
async def upload_files(
    files: List[UploadFile] = File(...),
    db: AsyncSession = Depends(get_db)
):
    uploaded_files = []
    for file in files:
        upload_data = save_uploaded_file(file)
        record = await create_upload(db, upload_data)
        uploaded_files.append(record)
    return uploaded_files


@router.get("/fichier", response_model=List[UploadResponse],tags=["Fichiers"])
async def list_uploads(db: AsyncSession = Depends(get_db)):
    return await get_all_uploads(db)

#-------------------------------
# Recommandations de cultures
#-------------------------------
@router.post("/recommandation", response_model=RecommendationResponse, tags=["Recommandations"])
async def obtenir_recommandations(
    request: RecommendationRequest,
    db: AsyncSession = Depends(get_db)
):
    """Obtenir les recommandations de culture pour une parcelle"""
    
    result_parcelle = await db.execute(
        select(Parcelle).where(Parcelle.id == request.parcelle_id)
    )
    parcelle = result_parcelle.scalars().first()
    
    if not parcelle:
        raise HTTPException(status_code=404, detail="Parcelle introuvable")
    
    result_analyse = await db.execute(
        select(AnalyseSol)
        .where(AnalyseSol.parcelle_id == request.parcelle_id)
        .order_by(AnalyseSol.created_at.desc())
        .limit(1)
    )
    analyse_sol = result_analyse.scalars().first()
    
    if not analyse_sol:
        raise HTTPException(status_code=404, detail="Aucune analyse de sol trouvée")
    
    region = request.region
    engine = RecommendationEngine()
    
    analyse_detaillee = engine.analyser_sol(analyse_sol.ph, analyse_sol.n, analyse_sol.p, analyse_sol.k, analyse_sol.humidite)
    
    cultures_region = engine.CULTURES_PAR_REGION.get(region, [])
    
    recommandations = []
    for culture in cultures_region:
        score, raisons = engine.calculer_score_aptitude(culture, analyse_sol.ph, analyse_sol.n, analyse_sol.p, analyse_sol.k)
        
        rec = CultureRecommendation(
            nom_culture=culture,
            aptitude=engine.obtenir_aptitude_label(score),
            rendement_potentiel=engine.obtenir_rendement_estime(culture, score),
            raisons=raisons if raisons else ["Conditions favorables"],
            pratiques_recommandees=engine.obtenir_pratiques_recommandees(culture, analyse_sol.ph, analyse_sol.humidite),
            besoins_irrigation="élevés" if analyse_sol.humidite < 30 else "modérés" if analyse_sol.humidite < 60 else "faibles",
            cycle_culture=120 if culture in ["mil", "sorgho"] else 150 if culture in ["mais", "riz"] else 180,
            score=score
        )
        recommandations.append(rec)
    
    recommandations.sort(key=lambda x: x.score, reverse=True)
    
    actions = []
    if analyse_sol.n < 20:
        actions.append("Appliquer un engrais azoté avant le semis")
    if analyse_sol.ph < 5.5 or analyse_sol.ph > 8:
        actions.append("Corriger le pH du sol")
    if analyse_sol.humidite < 20 and region == Region.SAHEL:
        actions.append("Mettre en place des techniques de conservation de l'eau")
    
    culture_principale = recommandations[0] if recommandations else None
    
    rec_data = {
        "parcelle_id": request.parcelle_id,
        "analyse_sol_id": analyse_sol.id,
        "region": region.value,
        "culture_principale": culture_principale.nom_culture if culture_principale else "aucune",
        "aptitude": culture_principale.aptitude if culture_principale else "faible",
        "score": culture_principale.score if culture_principale else 0,
        "rendement_potentiel": culture_principale.rendement_potentiel if culture_principale else "N/A",
        "raisons": culture_principale.raisons if culture_principale else [],
        "pratiques_recommandees": culture_principale.pratiques_recommandees if culture_principale else [],
        "amendements_recommandes": engine.generer_amendements(analyse_sol.ph, analyse_sol.n, analyse_sol.p, analyse_sol.k),
        "actions_prioritaires": actions,
        "analyse_detaillee": analyse_detaillee,
        "cultures_recommandees": [{"nom": r.nom_culture, "aptitude": r.aptitude, "score": r.score} for r in recommandations],
        "besoins_irrigation": culture_principale.besoins_irrigation if culture_principale else "N/A",
        "cycle_culture": culture_principale.cycle_culture if culture_principale else 0
    }
    
    db_rec = Recommandation(**rec_data)
    db.add(db_rec)
    await db.commit()
    
    return RecommendationResponse(
        parcelle_id=request.parcelle_id,
        region=region.value,
        analyseSol=AnalyseSolInfo(ph=analyse_sol.ph, n=analyse_sol.n, p=analyse_sol.p, k=analyse_sol.k, humidite=analyse_sol.humidite),
        analyse_detaillee=analyse_detaillee,
        cultures_recommandees=recommandations,
        actions_prioritaires=actions,
        amendements_recommandes=engine.generer_amendements(analyse_sol.ph, analyse_sol.n, analyse_sol.p, analyse_sol.k)
    )

# @router.get("/recommandation/{parcelle_id}", tags=["Recommandations"])
# async def obtenir_derniere_recommandation(parcelle_id: UUID, db: AsyncSession = Depends(get_db)):
#     """Récupère la dernière recommandation pour une parcelle"""
    
#     result = await db.execute(
#         select(Recommandation)
#         .where(Recommandation.parcelle_id == parcelle_id)
#         .order_by(Recommandation.created_at.desc())
#         .limit(1)
#     )
#     recommandation = result.scalars().first()
    
#     if not recommandation:
#         raise HTTPException(status_code=404, detail="Aucune recommandation trouvée")
    
#     return recommandation