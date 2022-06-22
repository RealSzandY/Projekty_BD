"""models_file_correction

Revision ID: a7c640b7e43f
Revises: 8862419bf2a5
Create Date: 2022-06-22 22:13:43.982776

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a7c640b7e43f'
down_revision = '8862419bf2a5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('book', sa.Column('author_id', sa.Integer(), nullable=True))
    op.drop_constraint(None, 'book', type_='foreignkey')
    op.create_foreign_key(None, 'book', 'author', ['author_id'], ['id'])
    op.drop_column('book', 'author')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('book', sa.Column('author', sa.INTEGER(), nullable=True))
    op.drop_constraint(None, 'book', type_='foreignkey')
    op.create_foreign_key(None, 'book', 'author', ['author'], ['full_name'])
    op.drop_column('book', 'author_id')
    # ### end Alembic commands ###