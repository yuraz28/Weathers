from datetime import date
from pydantic import BaseModel
from typing import List


class Continent(BaseModel):
    id_continent: int
    continent_name: str
    continent_img: str


class FullContinents(BaseModel):
    continents: List[Continent]


class Country(BaseModel):
    id_country: int
    id_continent: int
    country_name: str
    flag: str


class FullCountries(BaseModel):
    countries: List[Country]


class Citi(BaseModel):
    id_city: int
    id_country: int
    citi_name: str
    city_img: str


class FullCities(BaseModel):
    cities: List[Citi]


class Weather(BaseModel):
    id_weather: int
    id_city: int
    date: date
    weather_status: str
    status_icon: str
    wind_speed: int
    humidity: int
    temperature: int


class ThreeWeathers(BaseModel):
    weathers: List[Weather]
