"""Post timezones

Revision ID: f441fcdec380
Revises: 3bed7b8d8720
Create Date: 2019-10-04 17:03:42.111463

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f441fcdec380'
down_revision = '3bed7b8d8720'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('posts', 'timestamp', server_default=sa.text("TIMEZONE('utc', CURRENT_TIMESTAMP)"))


def downgrade():
    op.alter_column('posts', 'timestamp', server_default=sa.text('now()'))
