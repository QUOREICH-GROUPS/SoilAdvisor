from sqlalchemy import Column, Integer, Float, Date, String, ForeignKey
from app.database.base import Base

class ImageSatellite(Base):
    __tablename__ = "images_satellite"
    id = Column(Integer, primary_key=True, index=True)
    parcelle_id = Column(Integer, ForeignKey("parcelles.id"))
    ndvi = Column(Float)
    evi = Column(Float)
    mndwi = Column(Float)
    date_capture = Column(Date)
    source = Column(String)