#!/usr/bin/python3
"""Defines the User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    User class that inherits from BaseModel
    """

    email: str = ""
    password: str = ""
    first_name: str = ""
    last_name: str = ""
