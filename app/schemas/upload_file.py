from pydantic import BaseModel
from uuid import UUID


class UploadCreate(BaseModel):
    nom_fichier: str
    chemin_fichier: str
    type_fichier: str

class UploadResponse(BaseModel):
    id: UUID
    nom_fichier: str
    chemin_fichier: str
    type_fichier: str

    class Config:
        from_attributes = True