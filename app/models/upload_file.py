

import uuid
from sqlalchemy import UUID, Column, String
from app.database.base import Base


class Upload(Base):
    __tablename__="fichier"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    nom_fichier = Column(String(255), nullable=False)
    chemin_fichier = Column(String(500), nullable=False)
    type_fichier = Column(String(50), nullable=False)