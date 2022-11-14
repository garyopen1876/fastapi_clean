"""change TodoList user from user.id to user.username

Revision ID: 9f13b1d51bfe
Revises: c038a14a806f
Create Date: 2022-11-14 09:41:52.436072

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9f13b1d51bfe'
down_revision = 'c038a14a806f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('todolists', sa.Column('user', sa.String(), nullable=False))
    op.create_foreign_key(None, 'todolists', 'users', ['user'], ['username'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'todolists', type_='foreignkey')
    op.drop_column('todolists', 'user')
    # ### end Alembic commands ###