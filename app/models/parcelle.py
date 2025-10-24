from sqlalchemy import Column, Integer, String, Float
from geoalchemy2 import Geometry
from app.database.base import Base


class Parcelle(Base):
    __tablename__ = "parcelles"
    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String, index=True)
    geom = Column(Geometry("POLYGON", 4326))
    proprietaire_id = Column(Integer)
    surface_ha = Column(Float)