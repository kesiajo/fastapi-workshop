import mongoengine
from decouple import config


MONGODB_PRIVATE_SRV = config("MONGODB_PRIVATE_SRV", default="")
MONGODB_USERNAME = config("MONGODB_USERNAME", default="")
MONGODB_PASSWORD = config("MONGODB_PASSWORD", default="")
MONGODB_DB_NAME = config("MONGODB_DB_NAME")


def initialize_db() -> None:
    """Initialise DB Connection"""
    mongoengine.connect(
        host=MONGODB_PRIVATE_SRV,
        username=MONGODB_USERNAME,
        password=MONGODB_PASSWORD,
        db=MONGODB_DB_NAME,
    )
