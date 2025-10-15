from pydantic import BaseModel
from typing import Optional

# Schémas Pydantic
class ImageSatelliteResponse(ImageSatelliteCreate):
    id: int
    class Config:
        from_attributes = True