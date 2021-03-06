"""User private field

Revision ID: c0e517a11b26
Revises: 08a650a98aa0
Create Date: 2019-09-01 15:48:15.714764

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c0e517a11b26'
down_revision = '08a650a98aa0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('private', sa.Boolean(), server_default='false', nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'private')
    # ### end Alembic commands ###
