import logging

from backend.src.constant.error_constant import ErrorDetail
from backend.src.constant.success_constant import SuccessDetail
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
        logger.info(SuccessDetail.new_itinerary(new_itinerary.id))
    except Exception as e:
        session.rollback()
        logger.error(ErrorDetail.unknown("save_final_itinerary", e))
        raise

    return new_itinerary.id


def save_itinerary_message(itinerary_id: str, conversation_id: str):
    try:
        db = get_database()
        session = next(db)
        new_message = Message(
            conversation_id=conversation_id,
            sender="bot",
            category="itinerary",
            content=itinerary_id,
        )
        session.add(new_message)
        session.commit()
        logger.info(SuccessDetail.new_message(new_message.id))
    except Exception as e:
        session.rollback()
        logger.error(ErrorDetail.unknown("save_itinerary_message", e))
        raise
