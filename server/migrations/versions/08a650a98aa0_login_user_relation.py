"""Login/user relation

Revision ID: 08a650a98aa0
Revises: 09a329c81f0b
Create Date: 2019-08-30 15:52:55.978705

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '08a650a98aa0'
down_revision = '09a329c81f0b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('logins', sa.Column('user_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'logins', 'users', ['user_id'], ['id'])
    op.drop_constraint('users_logins_id_fkey', 'users', type_='foreignkey')
    op.drop_column('users', 'logins_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('logins_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('users_logins_id_fkey', 'users', 'logins', ['logins_id'], ['id'])
    op.drop_constraint(None, 'logins', type_='foreignkey')
    op.drop_column('logins', 'user_id')
    # ### end Alembic commands ###
