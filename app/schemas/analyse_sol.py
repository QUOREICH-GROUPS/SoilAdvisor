from pydantic import BaseModel
from datetime import datetime

class AnalyseSolCreate(BaseModel):
    parcelle_id: int
    ph: float
    n: float
    p: float
    k: float
    humidite: float

class AnalyseSolResponse(AnalyseSolCreate):
    id: int
    date_maj: datetime
    class Config:
        from_attributes = True