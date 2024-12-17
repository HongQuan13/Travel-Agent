"""Message table: change plan category to itinerary final

Revision ID: 38c5ccf4ee86
Revises: 77809746eb19
Create Date: 2024-12-17 22:53:06.423327

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "38c5ccf4ee86"
down_revision: Union[str, None] = "77809746eb19"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.execute(
        "UPDATE public.messages SET category = 'itinerary' WHERE category = 'plan'"
    )


def downgrade():
    op.execute(
        "UPDATE public.messages SET category = 'plan' WHERE category = 'itinerary'"
    )
