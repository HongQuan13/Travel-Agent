import logging

from backend.src.dbs.init_postgres import get_database
from backend.src.models.message_model import Message
from backend.src.models.plan_model import Plan

logging.basicConfig(level=logging.INFO, force=True)
logger = logging.getLogger(__name__)


def save_final_itinerary(plan_detail: str):
    db = get_database()
    session = next(db)
    new_plan = Plan(plan_detail=plan_detail)

    try:
        session.add(new_plan)
        session.commit()
        logger.info(f"Create new plan {new_plan.id} successfully")
    except Exception as e:
        session.rollback()
        logger.error(f"Error saving plan: {e}")
        raise

    return new_plan.id


def save_itinerary_message(plan_id: str):
    db = get_database()
    session = next(db)
    # hardcode conversation_id= 1
    new_message = Message(
        conversation_id=1,
        sender="bot",
        category="plan",
        message_text=plan_id,
    )

    try:
        session.add(new_message)
        session.commit()
        logger.info(f"Create new message {new_message.id} successfully")
    except Exception as e:
        session.rollback()
        logger.error(f"Error saving message: {e}")
        raise
