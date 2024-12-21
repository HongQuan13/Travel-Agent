import logging
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from backend.src.constant.error_constant import ErrorDetail
from backend.src.constant.success_constant import SuccessDetail

logger = logging.getLogger(__name__)


class Database:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
            cls._instance._engine_instance = None
            cls._instance._session_local = None
        return cls._instance

    def __init__(self):
        self._check_env()
        self._create_connection()

    def _check_env(self) -> None:
        connection_string = os.getenv("DB_CONNECTION_STRING")
        if connection_string == None:
            raise ValueError(
                f"Unable to access database connection string in .env file"
            )
        self.db_connection_string = connection_string

    def _create_connection(self):
        if self._engine_instance is None:
            try:
                self._engine_instance = create_engine(self.db_connection_string)
                self._session_local = sessionmaker(
                    autocommit=False, autoflush=False, bind=self._engine_instance
                )
                logger.info(SuccessDetail.db_connection)
            except Exception as e:
                logger.error(ErrorDetail.unknown("Database connection", e))
                self._engine_instance = None
                raise

    def get_engine(self):
        if self._engine_instance is None:
            self._create_connection()
        return self._engine_instance

    def get_session(self):
        if self._session_local is None:
            self._create_connection()
        return self._session_local()


def instance_postgres():
    db = Database()
    db.get_engine()


def get_database():
    db = Database().get_session()
    try:
        yield db
    finally:
        db.close()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, force=True)
    logger = logging.getLogger(__name__)
    load_dotenv()

    db = Database()
    engine_instance = db.get_engine()
    logger.info(f"Create new database engine sucessfully, {engine_instance}")
