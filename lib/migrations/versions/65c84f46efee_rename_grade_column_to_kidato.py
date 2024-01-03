"""Rename grade column to kidato

Revision ID: 65c84f46efee
Revises: 791279dd0760
Create Date: 2024-01-03 22:04:09.225407

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '65c84f46efee'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('students', 'grade', new_column_name='kidato')


def downgrade() -> None:
    op.alter_column('students', 'kidato', new_column_name='grade')
