#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
import models
from sqlalchemy import Column, String
from os import getenv


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    if models.t_stor == 'db':
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=False)
        last_name = Column(String(128), nullable=False)
    else:
        email = ''
        password = ''
        first_name = ''
        last_name = ''

    def __init__(self, *args, **kwargs):
        """initializes city"""
        super().__init__(*args, **kwargs)