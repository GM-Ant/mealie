"""Add recipe variations

Revision ID: 20250112_1047
Revises:
Create Date: 2025-01-12 10:47:00.000000

"""

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "20250112_1047"
down_revision: str | None = None
branch_labels: str | None = None
depends_on: str | None = None


def upgrade():
    # Add parent_id column
    op.add_column("recipes", sa.Column("parent_id", postgresql.UUID(), nullable=True))
    op.create_foreign_key("fk_recipes_parent_id", "recipes", "recipes", ["parent_id"], ["id"], ondelete="SET NULL")

    # Add is_variation column
    op.add_column("recipes", sa.Column("is_variation", sa.Boolean(), nullable=False, server_default="false"))
    op.create_index(op.f("ix_recipes_is_variation"), "recipes", ["is_variation"], unique=False)
    op.create_index(op.f("ix_recipes_parent_id"), "recipes", ["parent_id"], unique=False)


def downgrade():
    op.drop_index(op.f("ix_recipes_parent_id"), table_name="recipes")
    op.drop_index(op.f("ix_recipes_is_variation"), table_name="recipes")
    op.drop_constraint("fk_recipes_parent_id", "recipes", type_="foreignkey")
    op.drop_column("recipes", "is_variation")
    op.drop_column("recipes", "parent_id")
