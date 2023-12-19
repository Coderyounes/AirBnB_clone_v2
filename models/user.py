#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
import models
import sqlalchemy
from sqlalchemy import Column, String
from os import getenv
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    if models.t_stor == 'db':
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=False)
        last_name = Column(String(128), nullable=False)
        places = relationship("Place", cascade="all, delete-orphan", backref="user")
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""

    def __init__(self, *args, **kwargs):
        """initializes users"""
        super().__init__(*args, **kwargs)