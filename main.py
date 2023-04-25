from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from models import Base
from schemas import Citi, Country, Continent, Weather, \
    FullCities, FullCountries, FullContinents, ThreeWeathers
from crud import get_cities, get_countries, get_continents, get_weather
from database import SessionLocal, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def continents(db: Session = Depends(get_db)):
    continents_query = get_continents(db)
    return FullContinents(
        continents=[
            Continent(
                id_continent=i.id_continent,
                continent_name=i.continent_name,
                continent_img=i.continent_img
            ) for i in continents_query
        ]
    )


@app.get("/{id_continent}/")
def countries(id_continent: int, db: Session = Depends(get_db)):
    countries_query = get_countries(db, id_continent)
    return FullCountries(
        countries=[
            Country(
                id_country=i.id_country,
                id_continent=i.id_continent,
                country_name=i.country_name,
                flag=i.flag
            ) for i in countries_query
        ]
    )


@app.get("/{id_continent}/{id_country}")
def cities(id_continent: int, id_country: int, db: Session = Depends(get_db)):
    cities_query = get_cities(db, id_continent, id_country)
    return FullCities(
        cities=[
            Citi(
                id_city=i.Cities.id_city,
                id_country=i.Cities.id_country,
                citi_name=i.Cities.citi_name,
                city_img=i.Cities.city_img
            ) for i in cities_query
        ]
    )


@app.get("/{id_continent}/{id_country}/{id_city}/")
def weathers(id_continent: int, id_country: int, id_city: int, db: Session = Depends(get_db)):
    weathers_query = get_weather(db, id_continent, id_country, id_city)
    return ThreeWeathers(
        weathers=[
            Weather(
                id_weather=i.id_weather,
                id_city=i.id_city,
                date=i.date,
                weather_status=i.weather_status,
                status_icon=i.status_icon,
                wind_speed=i.wind_speed,
                humidity=i.humidity,
                temperature=i.temperature
            ) for i in weathers_query
        ]
    )
