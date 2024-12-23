"""Add title column to conversations

Revision ID: b3cfcc5f2a6b
Revises: 38c5ccf4ee86
Create Date: 2024-12-23 15:07:44.334502

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "b3cfcc5f2a6b"
down_revision: Union[str, None] = "38c5ccf4ee86"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    # Step 1: Add the column with a default value (nullable=True temporarily)
    op.add_column(
        "conversations",
        sa.Column("title", sa.String(), nullable=True, default="Default title"),
    )

    # Step 2: Set the default value 'Default title' for existing rows where the title is NULL
    op.execute("UPDATE conversations SET title = 'Default title' WHERE title IS NULL")

    # Step 3: Alter the column to set nullable=False (after updating existing rows)
    op.alter_column("conversations", "title", existing_type=sa.String(), nullable=False)


def downgrade():
    # Rollback: Drop the column if rolling back the migration
    op.drop_column("conversations", "title")
