"""migracion inicial

Revision ID: 6c021dadddb8
Revises: 89371cf94e51
Create Date: 2023-11-09 17:54:43.127438

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '6c021dadddb8'
down_revision = '89371cf94e51'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('comentario', schema=None) as batch_op:
        batch_op.alter_column('texto_comentario',
               existing_type=mysql.VARCHAR(length=500),
               type_=sa.String(length=100),
               existing_nullable=False)
        batch_op.alter_column('fecha_creacion',
               existing_type=mysql.VARCHAR(length=100),
               type_=sa.Date(),
               existing_nullable=False)

    with op.batch_alter_table('usuario', schema=None) as batch_op:
        batch_op.add_column(sa.Column('clave_hash', sa.String(length=100), nullable=False))
        batch_op.add_column(sa.Column('is_admin', sa.Boolean(), nullable=True))
        batch_op.create_unique_constraint(None, ['nombre'])
        batch_op.drop_column('clave')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('usuario', schema=None) as batch_op:
        batch_op.add_column(sa.Column('clave', mysql.VARCHAR(length=100), nullable=False))
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('is_admin')
        batch_op.drop_column('clave_hash')

    with op.batch_alter_table('comentario', schema=None) as batch_op:
        batch_op.alter_column('fecha_creacion',
               existing_type=sa.Date(),
               type_=mysql.VARCHAR(length=100),
               existing_nullable=False)
        batch_op.alter_column('texto_comentario',
               existing_type=sa.String(length=100),
               type_=mysql.VARCHAR(length=500),
               existing_nullable=False)

    # ### end Alembic commands ###
