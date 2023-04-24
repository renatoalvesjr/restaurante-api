from sqlalchemy import Column, Integer, String, Float

from database import Base

class Restaurant(Base):
    __tablename__ = "restaurant"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    address = Column(String, unique=True)
    phone = Column(String, unique=True, default=True)
    cnpj = Column(String(length=14), unique=True)
    rate = Column(Float(precision=2), unique=True)