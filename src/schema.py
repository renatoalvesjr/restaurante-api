from pydantic import BaseModel, Field

class CreateRestaurant(BaseModel):
    name: str
    address: str
    phone: str
    cnpj: str
    rate: float

class ReturnRestaurant(BaseModel):
    id: int
    name: str
    rate: float

class UpdateRestaurant(BaseModel):
    address: str
    phone: str
    rate: float