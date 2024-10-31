"""create table user, task

Revision ID: dca6dcd357e8
Revises: 
Create Date: 2024-10-31 21:27:24.688951

"""
from alembic import op
import sqlalchemy as sa

revision = 'dca6dcd357e8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
    sa.Column('username', sa.String(), nullable=True),
            sa.Column('password_hash', sa.String(), nullable=True),
            sa.Column('id', sa.Integer(), nullable=False),
            sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    op.create_table('tasks',
    sa.Column('title', sa.String(), nullable=True),
            sa.Column('description', sa.String(), nullable=True),
            sa.Column('status', sa.String(), nullable=True),
            sa.Column('user_id', sa.Integer(), nullable=True),
            sa.Column('id', sa.Integer(), nullable=False),
            sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
            sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('tasks')
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_table('users')
