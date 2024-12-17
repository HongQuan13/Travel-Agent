"""Rename column message_text to content

Revision ID: e5f497ae96d5
Revises: 85d0dbc2b9d2
Create Date: 2024-12-17 21:53:55.766116

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "e5f497ae96d5"
down_revision: Union[str, None] = "85d0dbc2b9d2"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    # Rename the column from message_text to content
    op.alter_column("messages", "message_text", new_column_name="content")


def downgrade():
    # Rollback the column rename if we need to downgrade the migration
    op.alter_column("messages", "content", new_column_name="message_text")
