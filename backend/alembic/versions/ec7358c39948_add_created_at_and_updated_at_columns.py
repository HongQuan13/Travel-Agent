"""Add created_at and updated_at columns

Revision ID: ec7358c39948
Revises: b3cfcc5f2a6b
Create Date: 2024-12-23 15:19:18.475666

"""

from datetime import datetime
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "ec7358c39948"
down_revision: Union[str, None] = "b3cfcc5f2a6b"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    # Add created_at and updated_at columns to all affected tables
    op.add_column(
        "conversations",
        sa.Column("created_at", sa.DateTime(), default=datetime.utcnow),
    )
    op.add_column(
        "conversations",
        sa.Column(
            "updated_at",
            sa.DateTime(),
            default=datetime.utcnow,
            onupdate=datetime.utcnow,
        ),
    )

    op.add_column(
        "itineraries",
        sa.Column("created_at", sa.DateTime(), default=datetime.utcnow),
    )
    op.add_column(
        "itineraries",
        sa.Column(
            "updated_at",
            sa.DateTime(),
            default=datetime.utcnow,
            onupdate=datetime.utcnow,
        ),
    )

    op.add_column(
        "messages",
        sa.Column("created_at", sa.DateTime(), default=datetime.utcnow),
    )
    op.add_column(
        "messages",
        sa.Column(
            "updated_at",
            sa.DateTime(),
            default=datetime.utcnow,
            onupdate=datetime.utcnow,
        ),
    )

    op.add_column(
        "users",
        sa.Column("created_at", sa.DateTime(), default=datetime.utcnow),
    )
    op.add_column(
        "users",
        sa.Column(
            "updated_at",
            sa.DateTime(),
            default=datetime.utcnow,
            onupdate=datetime.utcnow,
        ),
    )


def downgrade():
    # Drop the created_at and updated_at columns in case of rollback
    op.drop_column("conversations", "created_at")
    op.drop_column("conversations", "updated_at")

    op.drop_column("itineraries", "created_at")
    op.drop_column("itineraries", "updated_at")

    op.drop_column("messages", "created_at")
    op.drop_column("messages", "updated_at")

    op.drop_column("users", "created_at")
    op.drop_column("users", "updated_at")
