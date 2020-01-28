"""new user fields

Revision ID: 4337eba6dd58
Revises: 2a207e0d18a8
Create Date: 2020-01-28 20:59:07.491056

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4337eba6dd58'
down_revision = '2a207e0d18a8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###
