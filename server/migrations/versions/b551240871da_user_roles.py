"""User roles

Revision ID: b551240871da
Revises: f441fcdec380
Create Date: 2019-10-07 15:13:09.546196

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b551240871da'
down_revision = 'f441fcdec380'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    role = sa.Enum('banned', 'admin', 'user', name='role')
    role.create(op.get_bind())

    op.add_column('logins', sa.Column('role', sa.Enum('banned', 'admin', 'user', name='role'), server_default='user', nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('logins', 'role')

    role = sa.Enum('banned', 'admin', 'user', name='role')
    role.drop(op.get_bind())
    # ### end Alembic commands ###
