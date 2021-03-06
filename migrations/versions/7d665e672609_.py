"""empty message

Revision ID: 7d665e672609
Revises: e2c86ad35888
Create Date: 2021-04-28 03:34:13.146519

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7d665e672609'
down_revision = 'e2c86ad35888'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('provincias',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('nombre')
    )
    op.create_table('tiposServicio',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tipo', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('tipo')
    )
    op.create_table('tiposUsuario',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tipo', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('tipo')
    )
    op.create_table('cantones',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=120), nullable=False),
    sa.Column('provincias', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['provincias'], ['provincias.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('nombre')
    )
    op.create_table('pyme',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=120), nullable=False),
    sa.Column('provincia', sa.Integer(), nullable=False),
    sa.Column('canton', sa.Integer(), nullable=False),
    sa.Column('otrassenas', sa.String(length=80), nullable=False),
    sa.Column('servicio', sa.String(length=80), nullable=False),
    sa.Column('telefono', sa.String(length=80), nullable=False),
    sa.Column('facebook', sa.String(length=80), nullable=False),
    sa.Column('instragram', sa.String(length=80), nullable=False),
    sa.ForeignKeyConstraint(['canton'], ['cantones.id'], ),
    sa.ForeignKeyConstraint(['provincia'], ['provincias.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('nombre')
    )
    op.add_column('user', sa.Column('activo', sa.Boolean(), nullable=False))
    op.add_column('user', sa.Column('contrasena', sa.String(length=80), nullable=False))
    op.add_column('user', sa.Column('tipo', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'user', 'tiposUsuario', ['tipo'], ['id'])
    op.drop_column('user', 'is_active')
    op.drop_column('user', 'password')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('password', sa.VARCHAR(length=80), autoincrement=False, nullable=False))
    op.add_column('user', sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'user', type_='foreignkey')
    op.drop_column('user', 'tipo')
    op.drop_column('user', 'contrasena')
    op.drop_column('user', 'activo')
    op.drop_table('pyme')
    op.drop_table('cantones')
    op.drop_table('tiposUsuario')
    op.drop_table('tiposServicio')
    op.drop_table('provincias')
    # ### end Alembic commands ###
