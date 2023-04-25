from sqlalchemy.orm import Session
from models import Cities, Countries, Continents, Weathers


def get_continents(db: Session):
    return db.query(Continents).all()


def get_countries(db: Session, id_continent: int):
    return db.query(Countries).filter(Countries.id_continent == id_continent).all()


def get_cities(db: Session, id_continent: int, id_country: int):
    return db.query(Cities, Countries).join(Countries) \
      .filter(Cities.id_country == id_country) \
      .filter(Countries.id_continent == id_continent).all()


def get_weather(db: Session, id_continent: int, id_country: int, id_city: int):
    return db.query(Weathers)\
        .join(Cities).join(Countries) \
        .filter(Cities.id_city == id_city) \
        .filter(Cities.id_country == id_country) \
        .filter(Countries.id_continent == id_continent).limit(3).all()
