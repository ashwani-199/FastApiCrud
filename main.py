from fastapi import FastAPI, Depends
from typing import List
from sqlalchemy.orm import Session
from src.Query.QueryModel import Query
from src.DBService.services import get_db
from src.Models.place import Place

app = FastAPI()



# Routes for interacting with the API
@app.post('/places/', response_model=Place)
def create_places_view(place: Place, db: Session = Depends(get_db)):
    db_place = Query.create_place(db, place)
    return db_place

@app.get('/places/', response_model=List[Place])
def get_places_view(db: Session = Depends(get_db)):
    return Query.get_places(db)

@app.get('/place/{place_id}')
def get_place_view(place_id: int, db: Session = Depends(get_db)):
    return Query.get_place(db, place_id)


@app.delete('/place/{place_id}')
def delete_place_view(place_id: int, db: Session = Depends(get_db)):
    return Query.delete_place(db, place_id)

