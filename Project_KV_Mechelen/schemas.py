from pydantic import BaseModel

class SpelerBase(BaseModel):
    speler_nummer: int
    speler_naam: str
    speler_voornaam: str
    speler_positie: str

    class Config:
        orm_mode = True

class Speler(SpelerBase):
    speler_id: int

class SpelerCreate(SpelerBase):
    # speler_nummer: int
    speler_naam: str
    speler_voornaam: str
    speler_positie: str

# class ItemBase(BaseModel):
#     title: str
#     description: str | None = None
#
#
# class ItemCreate(ItemBase):
#     pass
#
#
# class Item(ItemBase):
#     id: int
#     owner_id: int
#
#     class Config:
#         orm_mode = True
#
#
# class SpelerBase(BaseModel):
#     email: str
#
#
# class UserCreate(SpelerBase):
#     password: str
#
#
# class Speler(SpelerBase):
#     id: int
#     is_active: bool
#     items: list[Item] = []
#
#     class Config:
#         orm_mode = True