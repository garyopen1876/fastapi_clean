"""create user table

Revision ID: cc2ba5882711
Revises: 
Create Date: 2022-09-23 09:24:17.554526

"""
from alembic import op
from sqlalchemy.schema import Sequence, CreateSequence, DropSequence
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cc2ba5882711'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute(CreateSequence(Sequence('user_id_seq')))
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###
    op.execute(DropSequence(Sequence('user_id_seq')))
