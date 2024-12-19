"""add assigned_tasks/models.py

Revision ID: df26d85ae1b5
Revises: 01b6a0c1aaa6
Create Date: 2024-12-19 17:13:12.540172

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'df26d85ae1b5'
down_revision: Union[str, None] = '01b6a0c1aaa6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('usertypes',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('usertypes', sa.String(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('type_user')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('type_user',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('type_users', sa.VARCHAR(), nullable=False),
    sa.Column('created_at', sa.DATETIME(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=False),
    sa.Column('updated_at', sa.DATETIME(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('usertypes')
    # ### end Alembic commands ###
