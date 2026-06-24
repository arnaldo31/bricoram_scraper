from seleniumbase import sb_cdp
import xml.etree.ElementTree as ET
import time
import json
from bs4 import BeautifulSoup
import pandas
import os
import subprocess
import platform

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Text, Float
from sqlalchemy.orm import declarative_base, sessionmaker
from openpyxl.cell.cell import ILLEGAL_CHARACTERS_RE

import threading

def clean_excel(value):
    if isinstance(value, str):
        return ILLEGAL_CHARACTERS_RE.sub("", value)
    return value



class TimeoutException(Exception):
    pass


def run_with_timeout(func, timeout, *args, **kwargs):
    result = []

    def wrapper():
        try:
            result.append(func(*args, **kwargs))
        except Exception as e:
            result.append(e)

    t = threading.Thread(target=wrapper)
    t.start()
    t.join(timeout)

    if t.is_alive():
        raise TimeoutException(f"{func.__name__} exceeded {timeout} seconds")

    if isinstance(result[0], Exception):
        raise result[0]

    return result[0]


SAVE_FOLDER = "./save"

os.makedirs(SAVE_FOLDER, exist_ok=True)

engine = create_engine(
    f"sqlite:///{SAVE_FOLDER}/bricoram.db",
    echo=False
)


Base = declarative_base()


class Profile(Base):
    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True)

    #category = Column(String(255))
    name = Column(String(255))

    intro_message = Column(Text)
    about = Column(Text)

    city_region = Column(String(255))
    email = Column(String(255))

    instagram = Column(String(255))
    tiktok = Column(String(255))
    youtube = Column(String(255))
    linkedin = Column(String(255))

    location = Column(String(255))
    phone = Column(String(100))

    reviews_count = Column(Integer)
    reviews_average = Column(Float)

    services = Column(Text)

    profile_image = Column(String(1000))
    website = Column(String(1000))

class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, autoincrement=True)
    profile_id = Column(Integer)
    client_name = Column(String(255))
    date = Column(String(100))
    rating = Column(Float)
    text = Column(Text)


class Image(Base):
    __tablename__ = "images"

    id = Column(Integer, primary_key=True, autoincrement=True)
    profile_id = Column(Integer)
    image_link = Column(String(1000))


class Price(Base):
    __tablename__ = "prices"

    id = Column(Integer, primary_key=True, autoincrement=True)
    profile_id = Column(Integer)
    title = Column(String(255))
    unit = Column(String(50))
    value = Column(Float)
