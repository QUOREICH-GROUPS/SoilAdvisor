from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey
from datetime import datetime
from app.database.base import Base

class AnalyseSol(Base):
    __tablename__ = "analyses_sol"
    id = Column(Integer, primary_key=True, index=True)
    parcelle_id = Column(Integer, ForeignKey("parcelles.id"))
    ph = Column(Float)
    n = Column(Float)
    p = Column(Float)
    k = Column(Float)
    humidite = Column(Float)
    date_maj = Column(DateTime, default=datetime.utcnow)