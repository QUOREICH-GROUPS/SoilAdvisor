from sqlalchemy import Column, Float, DateTime, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
import uuid
from app.database.base import Base

class ImageSatellite(Base):
    __tablename__ = "images_satellite"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    parcelle_id = Column(UUID(as_uuid=True), ForeignKey("parcelles.id"), nullable=False)

    ndvi = Column(Float, nullable=True)
    evi = Column(Float, nullable=True)
    mndwi = Column(Float, nullable=True)
    
    date_capture = Column(DateTime, nullable=True)
    source = Column(String, nullable=True)  # nom du satellite ou URL

    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
