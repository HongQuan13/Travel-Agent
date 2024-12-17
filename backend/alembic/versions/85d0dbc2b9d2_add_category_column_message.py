"""add category column -> message

Revision ID: 85d0dbc2b9d2
Revises: e1169cffaf1a
Create Date: 2024-12-17 14:27:29.039057

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "85d0dbc2b9d2"
down_revision: Union[str, None] = "e1169cffaf1a"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    category_enum = sa.Enum("text", "plan", name="category_enum")
    category_enum.create(op.get_bind(), checkfirst=True)

    # Add the 'category' column to the 'messages' table
    op.add_column(
        "messages",
        sa.Column(
            "category",
            category_enum,  # Use the created enum type here
            default="text",
        ),
    )


def downgrade() -> None:
    # Drop the 'category' column
    op.drop_column("messages", "category")

    # Drop the enum type (if no longer used in the database)
    category_enum = sa.Enum("text", "plan", name="category_enum")
    category_enum.drop(op.get_bind(), checkfirst=True)
