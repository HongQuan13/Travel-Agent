"""add plan schema again 1

Revision ID: a01389b7cfa0
Revises: 1e059cce8af4
Create Date: 2024-12-10 11:42:28.459921

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision: str = "a01389b7cfa0"
down_revision: Union[str, None] = "1e059cce8af4"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("messages")
    op.drop_table("conversations")
    op.drop_table("users")
    op.drop_table("plans")
    # ### end Alembic commands ###


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "messages",
        sa.Column("id", sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column("conversation_id", sa.INTEGER(), autoincrement=False, nullable=False),
        sa.Column(
            "sender",
            postgresql.ENUM("user", "bot", name="sender_enum"),
            autoincrement=False,
            nullable=False,
        ),
        sa.Column("message_text", sa.TEXT(), autoincrement=False, nullable=False),
        sa.Column(
            "timestamp", postgresql.TIMESTAMP(), autoincrement=False, nullable=True
        ),
        sa.ForeignKeyConstraint(
            ["conversation_id"], ["conversations.id"], name="fk_message_conversation_id"
        ),
        sa.PrimaryKeyConstraint("id", name="messages_pkey"),
    )
    op.create_table(
        "users",
        sa.Column(
            "id",
            sa.INTEGER(),
            server_default=sa.text("nextval('users_id_seq'::regclass)"),
            autoincrement=True,
            nullable=False,
        ),
        sa.Column(
            "username", sa.VARCHAR(length=30), autoincrement=False, nullable=False
        ),
        sa.Column("email", sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.PrimaryKeyConstraint("id", name="users_pkey"),
        sa.UniqueConstraint("email", name="uq_email"),
        postgresql_ignore_search_path=False,
    )
    op.create_table(
        "conversations",
        sa.Column("id", sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column("user_id", sa.INTEGER(), autoincrement=False, nullable=False),
        sa.ForeignKeyConstraint(
            ["user_id"], ["users.id"], name="fk_conversations_user_id"
        ),
        sa.PrimaryKeyConstraint("id", name="conversations_pkey"),
    )
    op.create_table(
        "plans",
        sa.Column("id", sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column("plan_detail", sa.VARCHAR(), autoincrement=False, nullable=False),
    )
    # ### end Alembic commands ###
