"""initial migration

Revision ID: 76088544e963
Revises: 
Create Date: 2024-06-25 18:01:24.886838

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '76088544e963'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('missions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_missions'))
    )
    op.create_table('planets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('distance_from_earth', sa.Integer(), nullable=True),
    sa.Column('nearest_star', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_planets'))
    )
    op.create_table('scientists',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('field_of_study', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_scientists'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('scientists')
    op.drop_table('planets')
    op.drop_table('missions')
    # ### end Alembic commands ###
