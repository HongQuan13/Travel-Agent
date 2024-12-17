"""Rename column plan_detail to itinerary_detail

Revision ID: 930f6aab3686
Revises: 315051f6eb04
Create Date: 2024-12-17 22:23:41.718036

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "930f6aab3686"
down_revision: Union[str, None] = "315051f6eb04"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.alter_column("itineraries", "plan_detail", new_column_name="itinerary_detail")


def downgrade():
    op.alter_column("itineraries", "itinerary_detail", new_column_name="plan_detail")
