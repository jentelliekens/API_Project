from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
# from sqlalchemy.orm import relationship

from database import Base

class Speler(Base):
    __tablename__ = "spelers"

    speler_id = Column(Integer, primary_key=True, index=True)
    speler_nummer = Column(Integer, index=True , unique=True)
    speler_naam = Column(String, index=True)
    speler_voornaam = Column(String, index=True)
    speler_positie = Column(String, index=True)





