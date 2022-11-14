"""delete TodoList user

Revision ID: c038a14a806f
Revises: 9727b242a0bb
Create Date: 2022-11-14 09:41:35.515263

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c038a14a806f'
down_revision = '9727b242a0bb'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('todolists_user_fkey', 'todolists', type_='foreignkey')
    op.drop_column('todolists', 'user')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('todolists', sa.Column('user', sa.INTEGER(), autoincrement=False, nullable=False))
    op.create_foreign_key('todolists_user_fkey', 'todolists', 'users', ['user'], ['id'])
    # ### end Alembic commands ###
