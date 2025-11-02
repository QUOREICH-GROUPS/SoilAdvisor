from datetime import datetime
from typing import Optional
from uuid import UUID, uuid4
from pydantic import BaseModel, Field


# -----------------------
# Schéma pour la création
# -----------------------
class ImageSatelliteCreate(BaseModel):
    name: str
    url: Optional[str] = None
    satellite_id: Optional[str] = None
    captured_at: Optional[datetime] = None


# -----------------------
# Schéma pour la mise à jour
# (toutes les valeurs optionnelles)
# -----------------------
class ImageSatelliteUpdate(BaseModel):
    name: Optional[str] = None
    url: Optional[str] = None
    satellite_id: Optional[str] = None
    captured_at: Optional[datetime] = None


# -----------------------
# Schéma de réponse
# -----------------------
class ImageSatelliteResponse(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    url: Optional[str]
    satellite_id: Optional[str]
    captured_at: Optional[datetime]
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}
