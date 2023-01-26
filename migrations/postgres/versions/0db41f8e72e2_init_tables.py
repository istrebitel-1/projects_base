"""init_tables

Revision ID: 0db41f8e72e2
Revises: 
Create Date: 2023-01-26 20:49:01.597119

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0db41f8e72e2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'dim_role',
        sa.Column('id', sa.INTEGER(), nullable=False),
        sa.Column(
            'name',
            sa.Enum('ADMIN', 'VIEWER', 'USER', name='user_role', schema='portal'),
            nullable=False,
        ),
        sa.Column('description', sa.Text(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        schema='portal'
    )

    op.create_table(
        'dim_user',
        sa.Column('id', sa.INTEGER(), nullable=False),
        sa.Column('username', sa.String(length=64), nullable=False),
        sa.Column('password_hash', sa.String(length=1024), nullable=False),
        sa.Column('name', sa.String(length=256), nullable=True),
        sa.Column('email', sa.String(length=256), nullable=True),
        sa.Column('is_active', sa.BOOLEAN(), server_default=sa.text('true'), nullable=False),
        sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
        sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('username'),
        schema='portal'
    )

    op.create_table(
        'map_user_role',
        sa.Column('id', sa.INTEGER(), nullable=False),
        sa.Column('role_id', sa.INTEGER(), nullable=True),
        sa.Column('user_id', sa.INTEGER(), nullable=True),
        sa.ForeignKeyConstraint(['role_id'], ['portal.dim_role.id'], ),
        sa.ForeignKeyConstraint(['user_id'], ['portal.dim_user.id'], ),
        sa.PrimaryKeyConstraint('id'),
        schema='portal'
    )


def downgrade() -> None:
    op.drop_table('map_user_role', schema='portal')
    op.drop_table('dim_user', schema='portal')
    op.drop_table('dim_role', schema='portal')

    op.execute('drop type portal.user_role;')
