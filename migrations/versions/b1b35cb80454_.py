"""empty message

Revision ID: b1b35cb80454
Revises: 
Create Date: 2024-06-12 19:44:39.513529

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b1b35cb80454'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=20), nullable=False),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_user_username'), ['username'], unique=True)

    op.create_table('files',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('filename', sa.String(length=64), nullable=False),
    sa.Column('mimetype', sa.String(length=16), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=False),
    sa.Column('owner_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['owner_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('files', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_files_filename'), ['filename'], unique=True)

    op.create_table('short_url',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('url', sa.String(length=128), nullable=False),
    sa.Column('short', sa.String(length=8), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('owner_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['owner_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('short_url', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_short_url_short'), ['short'], unique=True)
        batch_op.create_index(batch_op.f('ix_short_url_url'), ['url'], unique=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('short_url', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_short_url_url'))
        batch_op.drop_index(batch_op.f('ix_short_url_short'))

    op.drop_table('short_url')
    with op.batch_alter_table('files', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_files_filename'))

    op.drop_table('files')
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_user_username'))

    op.drop_table('user')
    # ### end Alembic commands ###