"""User routes."""

from typing import List, Optional

from fastapi import (
    APIRouter,
    Depends,
    FastAPI,
    File,
    HTTPException,
    Query,
    Request,
    UploadFile,
)
from fastapi.security import HTTPBearer
from fastapi_jwt_auth import AuthJWT
from sqlalchemy.orm import Session

from app.v1.utils.db import SessionLocal, engine
from app.v1.schema import users_crud, users_schema
from app.v1.model import users_model
from app.v1.utils.bcrypt import Bcrypt

bcrypt = Bcrypt()

# APIRouter creates path operations for item module
router = APIRouter(
    prefix="/api",
    tags=["API"],
    responses={404: {"description": "Not found"}},
)


# Dependency
def get_db():
    """Create a new SQLAlchemy SessionLocal.

    That will be used in a single request,
    and then close it once the request is finished.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/")
async def read_root():
    """Show base url."""
    return {"message": "Darareader Endpoint Working"}


@router.post("/user/", response_model=users_schema.User, dependencies=[Depends(HTTPBearer())])
async def read_item(
    user: users_schema.UserName,
    db: Session = Depends(get_db),
    authorize: AuthJWT = Depends(),
):
    """Read single item"""
    authorize.jwt_required()
    db_item = users_crud.get_user(db, username=user.username)

    if db_item is None:
        raise HTTPException(status_code=404, detail=f"User {user.username} not found ")

    return db_item


@router.post("/user/create", response_model=users_schema.User, dependencies=[Depends(HTTPBearer())])
async def create_user(
    user: users_schema.UserCreate,
    db: Session = Depends(get_db),
    authorize: AuthJWT = Depends(),
):
    """Read single item"""
    authorize.jwt_required()
    db_item = users_crud.create_user(
        db,
        name=user.name,
        lastname=user.lastname,
        username=user.username,
        password=user.password,
    )

    if db_item is None:
        raise HTTPException(status_code=404, detail=f"User {user.username} not found ")

    await users_crud.save_user_to_external_db(
        name=db_item.name,
        lastname=db_item.lastname,
        username=db_item.username,
        password=bcrypt.hash_password(db_item.password),
    )

    return db_item


@router.get("/user/top", response_model=List[users_schema.User], dependencies=[Depends(HTTPBearer())])
async def get_top(db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    """Get Top"""
    authorize.jwt_required()
    results = users_crud.get_users_top(db)
    return results


@router.get("/user/count", dependencies=[Depends(HTTPBearer())])
async def get_count(db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    """Get Count"""
    authorize.jwt_required()
    rows = users_crud.get_users_count(db)
    results = {"rows": rows}
    return results
