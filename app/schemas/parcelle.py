from pydantic import BaseModel
from typing import Optional

# Schémas Pydantic
class ParcelleCreate(BaseModel):
    nom: str
    #proprietaire_id: int
    surface_ha: float
    geom: Optional[str] = None

class ParcelleResponse(ParcelleCreate):
    id: int
    class Config:
        from_attributes = True