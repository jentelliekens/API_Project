from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud
import models
import schemas
from database import SessionLocal, engine
import os

if not os.path.exists('sqlitedb'):
    os.makedirs('sqlitedb')

#"sqlite:///./sqlitedb/sqlitedata.db"
models.Base.metadata.create_all(bind=engine)

kvMechelenApp = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@kvMechelenApp.post("/spelers/", response_model=schemas.Speler)
def create_speler(player: schemas.SpelerCreate, db: Session = Depends(get_db)):
    db_spelers = crud.get_speler_by_nummer(db, speler_nummer=player.speler_nummer)
    if db_spelers:
        raise HTTPException(status_code=400, detail="Nummer al in gebruik.")
    return crud.create_speler(db=db, player=player)


@kvMechelenApp.get("/spelers/", response_model=list[schemas.Speler])
def read_spelers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    spelers = crud.get_sperlers(db, skip=skip, limit=limit)
    return spelers


@kvMechelenApp.get("/speler/{speler_id}/", response_model=schemas.Speler)
def read_speler(speler_id: int, db: Session = Depends(get_db)):
    db_speler = crud.get_speler(db, speler_id=speler_id)
    if db_speler is None:
        raise HTTPException(status_code=404, detail="ID niet gevonden")
    return db_speler


@kvMechelenApp.delete("/speler/{speler_id}")
def delete_speler(speler_id: int, db: Session = Depends(get_db)):
    crud.delete_speler(db, speler_id=speler_id)
    return {"Speler is succesvol verwijderd."}

# @kvMechelenApp.get("/speler/{speler_nummer}/", response_model=schemas.Speler)
# def read_speler_2(speler_nummer: int, db: Session = Depends(get_db)):
#     db_speler_2 = crud.get_speler_by_nummer(db, speler_nummer=speler_nummer)
#     if db_speler_2 is None:
#         raise HTTPException(status_code=404, detail="Nummer niet gevonden")
#     return db_speler_2
