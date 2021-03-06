"""create test table

Revision ID: 447b9aa53e6
Revises: 
Create Date: 2015-10-19 10:56:12.365289

"""

# revision identifiers, used by Alembic.
revision = '447b9aa53e6'
down_revision = None
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('test',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('text', sa.String(length=256), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('test')
    ### end Alembic commands ###
