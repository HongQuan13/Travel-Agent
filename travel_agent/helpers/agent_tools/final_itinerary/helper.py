import logging

from backend.src.dbs.init_postgres import get_database
from backend.src.models.message_model import Message
from backend.src.models.itinerary_model import Itinerary

logging.basicConfig(level=logging.INFO, force=True)
logger = logging.getLogger(__name__)


def save_final_itinerary(itinerary_detail: str):
    try:
        db = get_database()
        session = next(db)
        new_itinerary = Itinerary(itinerary_detail=itinerary_detail)
        session.add(new_itinerary)
        session.commit()
        logger.info(f"Create new itinerary {new_itinerary.id} successfully")
    except Exception as e:
        session.rollback()
        logger.error(f"Error saving itinerary: {e}")
        raise

    return new_itinerary.id


def save_itinerary_message(itinerary_id: str):
    try:
        db = get_database()
        session = next(db)
        # hardcode conversation_id= 1
        new_message = Message(
            conversation_id=1,
            sender="bot",
            category="plan",
            content=itinerary_id,
        )
        session.add(new_message)
        session.commit()
        logger.info(f"Create new message {new_message.id} successfully")
    except Exception as e:
        session.rollback()
        logger.error(f"Error saving message: {e}")
        raise
