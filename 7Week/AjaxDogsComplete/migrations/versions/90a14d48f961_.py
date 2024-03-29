"""empty message

Revision ID: 90a14d48f961
Revises: 
Create Date: 2019-11-13 16:32:11.239146

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '90a14d48f961'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('dogs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=45), nullable=True),
    sa.Column('breed', sa.String(length=45), nullable=True),
    sa.Column('weight', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('dogs')
    # ### end Alembic commands ###
