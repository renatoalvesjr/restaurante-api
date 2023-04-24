from typing import Annotated, List

from fastapi import FastAPI, Path, Body,Response, HTTPException
from database import SessionLocal
from schema import CreateRestaurant, UpdateRestaurant, ReturnRestaurant
from model import Restaurant

app = FastAPI()

@app.post("/restaurants", response_model=CreateRestaurant)
def create_restaurant(item: CreateRestaurant):
    db = SessionLocal()
    db_restaurant = CreateRestaurant(name=item.name, address=item.address, phone=item.phone, cnpj=item.cnpj, rate=item.rate)
    db.add(db_restaurant)
    db.commit()
    db.refresh(db_restaurant)
    return db_restaurant

@app.get("/restaurants", response_model=List[ReturnRestaurant])
def return_all_restaurant():
    db = SessionLocal()
    restauraunts = db.query(Restaurant).all()
    return Restaurant

@app.get("/restaurants/{restaurant_id}", response_model=ReturnRestaurant)
def restaurant_by_id(restaurant_id: int):
    db = SessionLocal()
    db_restaurant = db.query(Restaurant).filter(Restaurant.id == restaurant_id).first()
    if db_restaurant is None:
        raise HTTPException(status_code=404, detail="Restaurant not found")
    return db_restaurant

@app.put("/restaurants/{restaurant_id}", response_model=UpdateRestaurant)
def update_restaurant(restaurant_id: int, restaurant: UpdateRestaurant):
    db = SessionLocal()
    db_restaurant = db.query(Restaurant).filter(Restaurant.id == restaurant_id).first()
    if db_restaurant is None:
        raise HTTPException(status_code=404, detail="Restaurant not found")
    if restaurant.address is not None:
        db_restaurant.address = restaurant.address
    if restaurant.phone is not None:
        db_restaurant.phone = restaurant.phone
    if restaurant.rate is not None:
        db_restaurant.rate = restaurant.rate
    db.commit()
    db.refresh(db_restaurant)
    return db_restaurant

@app.delete("/restaurants/{restaurant_id}")
def delete_item(restaurant_id: int):
    db = SessionLocal()
    db_restaurant = db.query(Restaurant).filter(Restaurant.id == restaurant_id).first()
    if db_restaurant is None:
        raise HTTPException(status_code=404, detail="Restaurant not found")
    db.delete(db_restaurant)
    db.commit()
    return {"message": "Restaurant deleted"}
