"""update users table

Revision ID: e25cb7c20fec
Revises: be73fdae2da9
Create Date: 2019-04-09 20:32:33.260563

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e25cb7c20fec'
down_revision = 'be73fdae2da9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('key', sa.String(length=80), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'key')
    # ### end Alembic commands ###