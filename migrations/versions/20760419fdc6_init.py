"""init

Revision ID: 20760419fdc6
Revises: 
Create Date: 2020-07-08 22:39:39.596977

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '20760419fdc6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('actors', 'gender')
    op.add_column('gender', sa.Column('actor_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'gender', 'actors', ['actor_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'gender', type_='foreignkey')
    op.drop_column('gender', 'actor_id')
    op.add_column('actors', sa.Column('gender', sa.BOOLEAN(), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
