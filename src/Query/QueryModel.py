from sqlalchemy.orm import declarative_base, sessionmaker, Session
from src.Models.place import DBPlace

class Query:
    def __init__(self) -> None:
        pass

    @staticmethod
    def get_place(db: Session, place_id: int):
        return db.query(DBPlace).where(DBPlace.id == place_id).first()

    @staticmethod
    def get_places(db: Session):
        return db.query(DBPlace).all()

    @staticmethod
    def create_place(db: Session, place: str):
        db_place = DBPlace(**place.dict())
        db.add(db_place)
        db.commit()
        db.refresh(db_place)

        return db_place
    
    @staticmethod
    def delete_place(db: Session, place_id: int):
        db_place = db.query(DBPlace).where(DBPlace.id == place_id).first()
        db.delete(db_place)
        db.commit()
        return {"message": "Item deleted successfully"}