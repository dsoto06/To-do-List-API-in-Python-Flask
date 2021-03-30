"""empty message

Revision ID: bcd3d6b56cb8
Revises: 762402052503
Create Date: 2021-03-30 02:51:43.343229

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bcd3d6b56cb8'
down_revision = '762402052503'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('to_do',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('label', sa.String(length=120), nullable=False),
    sa.Column('done', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('label')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('to_do')
    # ### end Alembic commands ###
