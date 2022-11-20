from sqlalchemy.orm import Session

import schemas
import models


def get_speler(db: Session, speler_id: int):
    return db.query(models.Speler).filter(models.Speler.speler_id == speler_id).first()


def get_speler_by_naam(db: Session, speler_naam: str):
    return db.query(models.Speler).filter(models.Speler.speler_naam == speler_naam).first()


def get_speler_by_nummer(db: Session, speler_nummer: int):
    return db.query(models.Speler).filter(models.Speler.speler_nummer == speler_nummer).first()


def get_sperlers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Speler).offset(skip).limit(limit).all()


def delete_speler(db: Session, speler_id: int):
    db.query(models.Speler).filter(models.Speler.speler_id == speler_id).delete()
    db.commit()


def create_speler(db: Session, player: schemas.SpelerCreate):
    db_spelers = models.Speler(speler_nummer=player.speler_nummer, speler_naam=player.speler_naam, speler_voornaam=player.speler_voornaam, speler_positie=player.speler_positie)
    db.add(db_spelers)
    db.commit()
    db.refresh(db_spelers)
    return db_spelers

