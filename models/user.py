#!/usr/bin/python3
""" holds class User"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import hashlib
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship



class User(BaseModel, Base):
    """Representation of a user """
    if models.storage_t == 'db':
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship("Place", backref="user")
        reviews = relationship("Review", backref="user")
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""

    def __init__(self, *args, **kwargs):
        """initializes user"""
        if kwargs:
            pwd = kwargs.pop("passowrd", None)
            if pwd:
                User.hash_password(self, pwd)
        super().__init__(*args, **kwargs)

    def hash_password(self, pwd):
        """Hhash password to a MD5 value"""
        hash = hashlib.md5()
        hash.update(pwd.encode("utf-8"))
        hash_pwd = hash.hexdigest()
        setattr(self, "password", hash_pwd)
