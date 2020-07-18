"""update relationship between actor and movie

Revision ID: 1c60d2a18076
Revises: 2f73d0356ba3
Create Date: 2020-07-18 23:26:46.963952

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1c60d2a18076'
down_revision = '2f73d0356ba3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('actors', sa.Column('movie_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'actors', 'movies', ['movie_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'actors', type_='foreignkey')
    op.drop_column('actors', 'movie_id')
    # ### end Alembic commands ###