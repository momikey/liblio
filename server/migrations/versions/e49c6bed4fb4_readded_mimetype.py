"""Readded mimetype

Revision ID: e49c6bed4fb4
Revises: 99eb78392b4e
Create Date: 2019-10-21 17:49:10.348964

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e49c6bed4fb4'
down_revision = '99eb78392b4e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('uploads', sa.Column('mimetype', sa.String(), server_default='application/octet-stream', nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('uploads', 'mimetype')
    # ### end Alembic commands ###
