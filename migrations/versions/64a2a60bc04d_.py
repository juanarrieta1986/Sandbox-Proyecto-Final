"""empty message

Revision ID: 64a2a60bc04d
Revises: 7d665e672609
Create Date: 2021-04-28 03:48:09.638084

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '64a2a60bc04d'
down_revision = '7d665e672609'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tiposusuario',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tipo', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('tipo')
    )
    op.drop_table('tiposUsuario')
    op.drop_constraint('user_tipo_fkey', 'user', type_='foreignkey')
    op.drop_column('user', 'tipo')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('tipo', sa.INTEGER(), autoincrement=False, nullable=False))
    op.create_foreign_key('user_tipo_fkey', 'user', 'tiposUsuario', ['tipo'], ['id'])
    op.create_table('tiposUsuario',
    sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"tiposUsuario_id_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('tipo', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='tiposUsuario_pkey'),
    sa.UniqueConstraint('tipo', name='tiposUsuario_tipo_key')
    )
    op.drop_table('tiposusuario')
    # ### end Alembic commands ###