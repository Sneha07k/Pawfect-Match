from sqlalchemy import Column, Integer, String, Boolean
from database import Base


class Pet(Base):
    __tablename__ = "pets"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, index=True)
    animal_type = Column(String, index=True)
    breed = Column(String)

    age = Column(Integer)
    gender = Column(String)
    size = Column(String)

    vaccinated = Column(Boolean)

    location = Column(String)
    description = Column(String)

    good_with_kids = Column(Boolean)
    good_with_pets = Column(Boolean)

    shelter_name = Column(String)
    contact_email = Column(String)

    image_url = Column(String)
