"""Rename table plans to itineraries

Revision ID: 315051f6eb04
Revises: e5f497ae96d5
Create Date: 2024-12-17 22:01:55.751748

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "315051f6eb04"
down_revision: Union[str, None] = "e5f497ae96d5"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    # Rename the table from plans to itineraries
    op.rename_table("plans", "itineraries")


def downgrade():
    # Rollback the table rename if necessary
    op.rename_table("itineraries", "plans")
