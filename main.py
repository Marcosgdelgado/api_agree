from app.v1.model.users_model import Users
from app.v1.utils.db import check_database, get_db


if __name__ == "__main__":
    flag = check_database()
    session = get_db()
    usuario = Users("MGD", "Testing")
    session.add(usuario)