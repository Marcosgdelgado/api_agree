"""Pydantic models.

Define attributes to do API request.
"""

from datetime import datetime
from typing import List

from pydantic import BaseModel


class UserBase(BaseModel):
    """Common attributes while creating o reading data."""

    username: str


class UserName(BaseModel):
    """Common attributes while creating o reading data."""

    username: str


class UserLogin(BaseModel):
    """Common attributes while creating o reading data."""

    username: str
    password: str


class UserCreate(UserBase):
    """Used when creating data."""

    password: str


class User(UserBase):
    """Used when reading data, when returning it from the API."""

    class Config:
        """Tell the Pydantic model to read the data even if it is not a dict."""

        orm_mode = True
