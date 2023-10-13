"""All API methods."""

import os
import uuid

from sqlalchemy import func
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import desc
from sqlalchemy.sql.functions import mode
from sqlalchemy.sql.sqltypes import Date, Integer

from app.v1.schema import users_schema, users_crud
from app.v1.utils.asyncio import async_post_request, async_get_request


def get_user(db: Session, username: str):
    """Return data for a single User Item."""
    return db.query(users_schema.User).filter(users_schema.User.username == username).first()


def authorize_user(db: Session, username: str, password: str):
    """Return data for a single User Item."""
    return (
        db.query(users_schema.User)
        .filter(users_schema.User.username == username, users_schema.User.password == password)
        .first()
    )


def get_users_top(db: Session):
    """Return data for all Users."""
    return db.query(users_schema.User).limit(5).all()


def get_users_count(db: Session):
    """Return row count of Users."""
    rows = db.query(users_schema.User.username).count()
    return rows


def create_user(db: Session, name: str, lastname: str, username: str, password: str):
    """Create User"""
    user = users_schema.User(username=username, password=password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


async def get_user_to_external_db(username: str):
    """Get User from external DB"""
    EXTERNAL_DB = os.getenv("EXTERNAL_DB")
    url = f"{EXTERNAL_DB}/users/{username}"
    user = await async_get_request(url)
    if user:
        return user
    return None


async def save_user_to_external_db(name: str, lastname: str, username: str, password: str):
    """Save User to external DB"""
    EXTERNAL_DB = os.getenv("EXTERNAL_DB")
    url = f"{EXTERNAL_DB}/users"
    data = {
        "id": str(uuid.uuid4()),
        "name": name,
        "lastname": lastname,
        "username": username,
        "password": password,
    }
    await async_post_request(url, data)
