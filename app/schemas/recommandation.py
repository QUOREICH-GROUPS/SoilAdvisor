from enum import Enum
from typing import List, Optional
from uuid import UUID
from pydantic import BaseModel


class Region(str, Enum):
    SAHEL = "sahel"
    SAVANE = "savane"
    GUINEEN = "guineen"
    FORET = "foret"

class CultureRecommendation(BaseModel):
    """Recommandation pour une culture"""
    nom_culture: str
    aptitude: str  # "excellente", "bonne", "moyenne", "faible"
    rendement_potentiel: str  # kg/ha estimé
    raisons: List[str]
    pratiques_recommandees: List[str]
    besoins_irrigation: str
    cycle_culture: int  # jours
    score: float  # 0-100

class AnalyseSolInfo(BaseModel):
    """Informations d'analyse du sol"""
    ph: float
    n: float
    p: float
    k: float
    humidite: float

class RecommendationResponse(BaseModel):
    """Réponse avec recommandations"""
    parcelle_id: UUID
    region: str
    analyseSol: AnalyseSolInfo
    analyse_detaillee: dict
    cultures_recommandees: List[CultureRecommendation]
    actions_prioritaires: List[str]
    amendements_recommandes: Optional[List[str]]

class RecommendationRequest(BaseModel):
    """Demande de recommandation"""
    parcelle_id: UUID
    region: Region
    # Les données de sol seront récupérées de AnalyseSol via parcelle_id

# class RecommandationCreate(BaseModel):
#     """Données pour créer une recommandation"""
#     parcelle_id: UUID
#     analyse_sol_id: UUID
#     region: str
#     culture_principale: str
#     aptitude: str
#     score: float
#     rendement_potentiel: str
#     raisons: List[str]
#     pratiques_recommandees: List[str]
#     amendements_recommandes: Optional[List[str]]
#     actions_prioritaires: List[str]
#     analyse_detaillee: dict
#     cultures_recommandees: List
#     besoins_irrigation: str
#     cycle_culture: int

# class RecommandationRead(BaseModel):
#     """Lecture d'une recommandation"""
#     id: UUID
#     parcelle_id: UUID
#     analyse_sol_id: UUID
#     region: str
#     culture_principale: str
#     aptitude: str
#     score: float
#     rendement_potentiel: str
#     raisons: List[str]
#     pratiques_recommandees: List[str]
#     amendements_recommandes: Optional[List[str]]
#     actions_prioritaires: List[str]
#     analyse_detaillee: dict
#     cultures_recommandees: List[dict]
#     besoins_irrigation: str
#     cycle_culture: int
    

#     class Config:
#         from_attributes = True