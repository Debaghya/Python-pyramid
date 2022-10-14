"""Initial table creation

Revision ID: 61edacb97d37
Revises: f62f83c76f27
Create Date: 2022-10-11 15:37:09.920495

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '61edacb97d37'
down_revision = 'f62f83c76f27'
branch_labels = None
depends_on = None


def upgrade() -> None:
    user_table = sa.table('users',
                          sa.Column('id', sa.Integer(), nullable=False),
                          sa.Column('username', sa.Text(), nullable=False),
                          sa.Column('password', sa.Text(), nullable=False),
                          sa.Column('first_name', sa.Text(), nullable=False),
                          sa.Column('last_name', sa.Text(), nullable=True),

                          )

    op.bulk_insert(user_table,
                   [
                       {'username': 'Batman',
                        'password': 'Alfred07',
                        'first_name': 'Bruce',
                        'last_name': 'Wayne'
                        },

                       {'username': 'WonderWoman',
                        'password': 'Trevour',
                        'first_name': 'Dianna',
                        'last_name': 'Prince'
                        }

                   ]
                   )


def downgrade() -> None:
    pass
