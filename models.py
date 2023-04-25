from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

engine = create_engine("mysql+mysqlconnector://root:password@localhost/bd", echo=True)

Base = declarative_base()


class Continents(Base):
    __tablename__ = 'Continents'

    id_continent = Column(Integer, primary_key=True)
    continent_name = Column(String(250), nullable=False)
    continent_img = Column(String(250), nullable=False)


class Countries(Base):
    __tablename__ = 'Countries'

    id_country = Column(Integer, primary_key=True)
    id_continent = Column(Integer, ForeignKey("Continents.id_continent"))
    country_name = Column(String(250), nullable=True)
    flag = Column(String(250), nullable=False)


class Cities(Base):
    __tablename__ = 'Cities'

    id_city = Column(Integer, primary_key=True)
    id_country = Column(Integer, ForeignKey("Countries.id_country"))
    citi_name = Column(String(250), nullable=True)
    city_img = Column(String(250), nullable=False)


class Weathers(Base):
    __tablename__ = 'Weathers'

    id_weather = Column(Integer, primary_key=True)
    id_city = Column(Integer, ForeignKey("Cities.id_city"))
    date = Column(DateTime(), nullable=False)
    weather_status = Column(String(250), nullable=False)
    status_icon = Column(String(250), nullable=False)
    wind_speed = Column(Integer)
    humidity = Column(Integer)
    temperature = Column(Integer)


Base.metadata.create_all(engine)
