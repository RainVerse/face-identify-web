# coding: utf-8
from sqlalchemy import Column, DateTime, Integer, String, text

from face_recognize import db

Base = db.Model
metadata = Base.metadata


class Image(Base):
    __tablename__ = 'image'

    id = Column(Integer, primary_key=True)
    url = Column(String(100), nullable=False)
    tester_id = Column(Integer)
    upload_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))


class Tester(Base):
    __tablename__ = 'tester'

    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    info = Column(String(100))
