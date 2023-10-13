from sqlalchemy.orm import Session
from app.v1.model.cliente_model import Cliente


def create_client(db: Session, name: str, id: int):
    """Create User"""
    user = Cliente(id=id, nombre=name)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
