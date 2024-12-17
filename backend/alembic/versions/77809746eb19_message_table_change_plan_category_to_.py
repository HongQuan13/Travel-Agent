"""Message table: change plan category to itinerary

Revision ID: 77809746eb19
Revises: 930f6aab3686
Create Date: 2024-12-17 22:42:07.886121

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "77809746eb19"
down_revision: Union[str, None] = "930f6aab3686"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    # Step 1: Add 'itinerary' to the enum category_enum
    op.execute("ALTER TYPE category_enum ADD VALUE 'itinerary'")


def downgrade():
    # In the downgrade, there is no easy way to remove an enum value in PostgreSQL,
    # so we would need a workaround similar to the original upgrade procedure to revert this change.
    # Since we are just adding a value, no changes need to be made in the downgrade for this operation.
    pass
