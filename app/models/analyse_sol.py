import uuid
from datetime import datetime
from sqlalchemy import Column, Float, DateTime, ForeignKey, func
from sqlalchemy.dialects.postgresql import UUID
from app.database.base import Base

class AnalyseSol(Base):
    __tablename__ = "analyses_sol"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    parcelle_id = Column(UUID(as_uuid=True), ForeignKey("parcelles.id"), nullable=False)
    ph = Column(Float)
    n = Column(Float)
    p = Column(Float)
    k = Column(Float)
    humidite = Column(Float)
    date_maj = Column(DateTime, default=datetime.now())
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)