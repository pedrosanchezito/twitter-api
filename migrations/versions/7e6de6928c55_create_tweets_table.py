"""Create tweets table

Revision ID: 7e6de6928c55
Revises:
Create Date: 2019-04-04 16:21:17.736416

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7e6de6928c55'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tweets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('text', sa.String(length=280)),
    sa.Column('created_at', sa.DateTime()),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tweets')
    # ### end Alembic commands ###
