from pydantic import BaseModel, EmailStr
from typing import Optional


class PetBase(BaseModel):
    name: str
    animal_type: str
    breed: str
    age: int
    gender: str
    size: str
    vaccinated: bool
    location: str
    description: Optional[str] = None
    good_with_kids: bool
    good_with_pets: bool
    shelter_name: str
    contact_email: EmailStr
    image_url: Optional[str] = None


class PetCreate(PetBase):
    pass


class PetUpdate(PetBase):
    pass


class PetResponse(PetBase):
    id: int

    class Config:
        from_attributes = True
