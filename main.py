from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Optional

import models, schemas, crud
from database import engine, SessionLocal, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()


# DB Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/pets/filter", response_model=list[schemas.PetResponse])
def filter_pets(
    animal_type: Optional[str] = None,
    breed: Optional[str] = None,
    location: Optional[str] = None,
    vaccinated: Optional[bool] = None,
    good_with_kids: Optional[bool] = None,
    good_with_pets: Optional[bool] = None,
    db: Session = Depends(get_db),
):
    return crud.filter_pets(
        db,
        animal_type,
        breed,
        location,
        vaccinated,
        good_with_kids,
        good_with_pets,
    )


@app.post("/pets", response_model=schemas.PetResponse)
def create_pet(pet: schemas.PetCreate, db: Session = Depends(get_db)):
    return crud.create_pet(db, pet)


@app.get("/pets", response_model=list[schemas.PetResponse])
def read_pets(db: Session = Depends(get_db)):
    return crud.get_pets(db)


@app.get("/pets/{pet_id}", response_model=schemas.PetResponse)
def read_pet(pet_id: int, db: Session = Depends(get_db)):
    pet = crud.get_pet(db, pet_id)
    if not pet:
        raise HTTPException(status_code=404, detail="Pet not found")
    return pet


@app.delete("/pets/{pet_id}")
def delete_pet(pet_id: int, db: Session = Depends(get_db)):
    pet = crud.delete_pet(db, pet_id)
    if not pet:
        raise HTTPException(status_code=404, detail="Pet not found")
    return {"message": "Pet deleted"}


@app.put("/pets/{pet_id}", response_model=schemas.PetResponse)
def update_pet(
    pet_id: int,
    pet: schemas.PetUpdate,
    db: Session = Depends(get_db)
):
    updated_pet = crud.update_pet(db, pet_id, pet)

    if not updated_pet:
        raise HTTPException(status_code=404, detail="Pet not found")

    return updated_pet




