"""Initial migration

Revision ID: 68f3320583ac
Revises: 
Create Date: 2024-08-06 16:52:14.906092

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '68f3320583ac'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_user_email'), ['email'], unique=True)
        batch_op.create_index(batch_op.f('ix_user_username'), ['username'], unique=True)

    op.create_table('recipe',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=140), nullable=True),
    sa.Column('ingredients', sa.String(length=140), nullable=True),
    sa.Column('steps', sa.Text(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('picture', sa.String(length=200), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='fk_user_id'),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('recipe', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_recipe_ingredients'), ['ingredients'], unique=False)

    op.create_table('review',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('recipe_id', sa.Integer(), nullable=True),
    sa.Column('rating', sa.Integer(), nullable=True),
    sa.Column('body', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['recipe_id'], ['recipe.id'], name='fk_recipe_id'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('review')
    with op.batch_alter_table('recipe', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_recipe_ingredients'))

    op.drop_table('recipe')
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_user_username'))
        batch_op.drop_index(batch_op.f('ix_user_email'))

    op.drop_table('user')
    # ### end Alembic commands ###
