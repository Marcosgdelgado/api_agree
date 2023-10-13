from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
from app.v1.utils.settings import Settings

settings = Settings()

# Define la URL de conexión a tu base de datos MySQL
db_url = f'mysql+mysqlconnector://{settings.db_user}:{settings.db_pass}@{settings.db_host}/{settings.db_name}'
# Intenta crear una conexión al motor de la base de datos
engine = create_engine(db_url)

# Intenta ejecutar una consulta SQL para verificar la conexión
if not database_exists(engine.url):
    create_database(engine.url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

Base.metadata.create_all(bind=engine)

engine.dispose()

def check_database():
    """Check if database is available."""
    try:
        engine.connect()
        return True
    except OperationalError:
        return False


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
