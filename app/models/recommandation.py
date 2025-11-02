# models/recommandation.py
import uuid
from datetime import datetime
from sqlalchemy import UUID, Column, Integer, String, Float, ForeignKey, DateTime, Text, func, JSON
from app.database.base import Base

class Recommandation(Base):
    __tablename__ = "recommandations"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    parcelle_id = Column(UUID(as_uuid=True), ForeignKey("parcelles.id"), nullable=False, index=True)
    analyse_sol_id = Column(UUID(as_uuid=True), ForeignKey("analyses_sol.id"), nullable=False)
    region = Column(String(50), nullable=False)  # sahel, savane, guineen, foret
    
    # Culture recommandée principale
    culture_principale = Column(String(100), nullable=False)
    aptitude = Column(String(50), nullable=False)  # excellente, bonne, moyenne, faible
    score = Column(Float, nullable=False)
    rendement_potentiel = Column(String(100))
    
    # Données JSON pour stocker les listes
    raisons = Column(JSON)  # List[str]
    pratiques_recommandees = Column(JSON)  # List[str]
    amendements_recommandes = Column(JSON)  # List[str]
    actions_prioritaires = Column(JSON)  # List[str]
    
    # Analyse détaillée
    analyse_detaillee = Column(JSON)  # dict
    cultures_recommandees = Column(JSON)  # List de toutes les cultures recommandées
    
    besoins_irrigation = Column(String(50))
    cycle_culture = Column(Integer)  # en jours
    
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
    date_maj = Column(DateTime, default=datetime.now())