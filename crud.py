from sqlalchemy.orm import Session
import models, schemas


def create_pet(db: Session, pet: schemas.PetCreate):
    db_pet = models.Pet(**pet.dict())
    db.add(db_pet)
    db.commit()
    db.refresh(db_pet)
    return db_pet


def get_pets(db: Session):
    return db.query(models.Pet).all()


def get_pet(db: Session, pet_id: int):
    return db.query(models.Pet).filter(models.Pet.id == pet_id).first()


def delete_pet(db: Session, pet_id: int):
    pet = get_pet(db, pet_id)
    if pet:
        db.delete(pet)
        db.commit()
    return pet


def update_pet(db: Session, pet_id: int, pet_update: schemas.PetUpdate):
    pet = db.query(models.Pet).filter(models.Pet.id == pet_id).first()

    if not pet:
        return None

    update_data = pet_update.dict(exclude_unset=True)

    for field, value in update_data.items():
        setattr(pet, field, value)

    db.commit()
    db.refresh(pet)

    return pet


def filter_pets(
    db: Session,
    animal_type: str | None = None,
    breed: str | None = None,
    location: str | None = None,
    vaccinated: bool | None = None,
    good_with_kids: bool | None = None,
    good_with_pets: bool | None = None,
):
    query = db.query(models.Pet)

    if animal_type:
        query = query.filter(models.Pet.animal_type == animal_type)

    if breed:
        query = query.filter(models.Pet.breed == breed)

    if location:
        query = query.filter(models.Pet.location == location)

    if vaccinated is not None:
        query = query.filter(models.Pet.vaccinated == vaccinated)

    if good_with_kids is not None:
        query = query.filter(models.Pet.good_with_kids == good_with_kids)

    if good_with_pets is not None:
        query = query.filter(models.Pet.good_with_pets == good_with_pets)

    return query.all()

