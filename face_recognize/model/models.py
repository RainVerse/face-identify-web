# coding: utf-8
from sqlalchemy import Column, DateTime, Integer, String, text

from face_recognize import db

Base = db.Model
metadata = Base.metadata


class DeepidRecord(Base):
    __tablename__ = 'deepid_record'

    id = Column(Integer, primary_key=True)
    record_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    record_comment = Column(String(50))
    record_result = Column(Integer)
    record_index = Column(Integer, nullable=False)


class Image(Base):
    __tablename__ = 'image'

    id = Column(Integer, primary_key=True)
    url = Column(String(200), nullable=False)
    upload_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    valid = Column(Integer, nullable=False, server_default=text("'1'"))


class Tester(Base):
    __tablename__ = 'tester'

    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    info = Column(String(100))
