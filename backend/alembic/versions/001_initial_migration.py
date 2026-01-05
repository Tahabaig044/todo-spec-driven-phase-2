"""Initial migration

Revision ID: 001
Revises:
Create Date: 2025-12-29 00:00:00.000000

"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '001'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Create tasks table
    op.create_table(
        'tasks',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('title', sa.String(length=255), nullable=False),
        sa.Column('description', sa.String(length=1000), nullable=True),
        sa.Column('completed', sa.Boolean(), nullable=False, default=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('id')
    )

    # Create index for id
    op.create_index(op.f('ix_tasks_id'), 'tasks', ['id'], unique=True)

    # Create index for completed field for efficient filtering
    op.create_index(op.f('ix_tasks_completed'), 'tasks', ['completed'], unique=False)


def downgrade() -> None:
    # Drop index for completed field
    op.drop_index(op.f('ix_tasks_completed'), table_name='tasks')

    # Drop index for id
    op.drop_index(op.f('ix_tasks_id'), table_name='tasks')

    # Drop tasks table
    op.drop_table('tasks')