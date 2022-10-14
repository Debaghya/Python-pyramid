"""Initial table creation

Revision ID: f62f83c76f27
Revises: 
Create Date: 2022-10-11 15:35:57.591123

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f62f83c76f27'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('username', sa.Text(), unique=True),
        sa.Column('password', sa.Text(), unique=False),
        sa.Column('first_name', sa.Text(), unique=False),
        sa.Column('last_name', sa.Text(), unique=False),

        sa.PrimaryKeyConstraint('id', name=op.f('pk_models01')),
    )


def downgrade() -> None:
    op.drop_table('users')
