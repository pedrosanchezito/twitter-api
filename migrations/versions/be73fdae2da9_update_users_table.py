"""update users table

Revision ID: be73fdae2da9
Revises: 2469cf814ea2
Create Date: 2019-04-09 20:31:23.989726

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'be73fdae2da9'
down_revision = '2469cf814ea2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'key')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('key', sa.VARCHAR(length=80), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
