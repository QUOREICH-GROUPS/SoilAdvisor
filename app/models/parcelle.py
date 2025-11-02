from sqlalchemy import Column, String, Float, DateTime
from sqlalchemy.dialects.postgresql import UUID
from geoalchemy2 import Geometry
from sqlalchemy.sql import func
import uuid
from app.database.base import Base

class Parcelle(Base):
    __tablename__ = "parcelles"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    nom = Column(String, index=True, nullable=False)
    geom = Column(Geometry("POLYGON", srid=4326), nullable=False)
    #proprietaire_id = Column(UUID(as_uuid=True), nullable=True)  # si le propriétaire est aussi UUID
    surface_ha = Column(Float, nullable=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
