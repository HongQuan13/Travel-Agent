import logging
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

logger = logging.getLogger(__name__)


class Database:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
            cls._instance._engine_instance = None
        return cls._instance

    def __init__(self):
        self._check_env()
        self._create_connection()

    def _check_env(self) -> None:
        connection_string = os.getenv("POSTGRES_CONNECTION_STRING")
        if connection_string == None:
            raise ValueError(
                f"Unable to access database connection string in .env file"
            )
        self.db_connection_string = connection_string

    def _create_connection(self):
        if self._engine_instance is None:
            self._engine_instance = create_engine(self.db_connection_string)
            logger.info("Database connection established!")

    def get_instance(self):
        if self._engine_instance is None:
            self._create_connection()
        return self._engine_instance


def instancePostgres():
    db = Database()
    db.get_instance()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, force=True)
    logger = logging.getLogger(__name__)
    load_dotenv()

    db = Database()
    engine_instance = db.get_instance()
    logger.info(f"Create new database engine sucessfully, {engine_instance}")
