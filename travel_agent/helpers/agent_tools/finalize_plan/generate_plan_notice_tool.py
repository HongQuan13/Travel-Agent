import logging
from langchain_core.tools import StructuredTool

from travel_agent.helpers.agent_tools.finalize_plan.models import PlanGenerateNotice

logging.basicConfig(level=logging.INFO, force=True)
logger = logging.getLogger(__name__)


def notice_generate_plan_successful(plan_title: str):
    """Use the tool."""
    logger.info(f"notice_generate_plan_successful called")
    return f"Plan {plan_title} is generated successfully"


notice_generate_plan_successful_tool = StructuredTool.from_function(
    func=notice_generate_plan_successful,
    name="notice_generate_plan_successful_tool",
    description="""Use to notice user, deep research final plan generated successfully""",
    args_schema=PlanGenerateNotice,
)
