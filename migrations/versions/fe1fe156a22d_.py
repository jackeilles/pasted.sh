"""empty message

Revision ID: fe1fe156a22d
Revises: b68b8fb2fde4
Create Date: 2024-08-07 23:43:28.517256

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fe1fe156a22d'
down_revision = 'b68b8fb2fde4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('files', schema=None) as batch_op:
        batch_op.add_column(sa.Column('mgmt', sa.String(), nullable=True))

    with op.batch_alter_table('short_url', schema=None) as batch_op:
        batch_op.add_column(sa.Column('mgmt', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('short_url', schema=None) as batch_op:
        batch_op.drop_column('mgmt')

    with op.batch_alter_table('files', schema=None) as batch_op:
        batch_op.drop_column('mgmt')

    # ### end Alembic commands ###