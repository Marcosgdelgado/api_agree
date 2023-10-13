from pydantic import BaseModel


class ClientBase(BaseModel):
    """Common attributes while creating o reading data."""

    id: int
    name: str = None
    id_categoria: int


class ClientCreate(ClientBase):
    id: int
    name: str


class Client(ClientBase):
    """Used when reading data, when returning it from the API."""

    class Config:
        """Tell the Pydantic model to read the data even if it is not a dict."""

        orm_mode = True
