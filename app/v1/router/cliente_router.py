from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from fastapi import Body
from sqlalchemy.orm import Session

from app.v1.schema import cliente_shema, cliente_crud
#from app.v1.service import user_service

from app.v1.utils.db import get_db


router = APIRouter(prefix="/api/v1")


@router.post(
    "/client/",
    tags=["clients"],
    status_code=status.HTTP_201_CREATED,
    response_model=cliente_shema.Client,
    #dependencies=[Depends(get_db)],
    summary="Create a new client"
)
def create_client(client: cliente_shema.ClientCreate, db: Session = Depends(get_db)):
    """
    ## Create a new user in the app

    ### Args
    The app can recive next fields into a JSON
    - email: A valid email
    - username: Unique username
    - password: Strong password for authentication

    ### Returns
    - user: User info
    """
    return cliente_crud.create_client(db, client.name, client.id)
