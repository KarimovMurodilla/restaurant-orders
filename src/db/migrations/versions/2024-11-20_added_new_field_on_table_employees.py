"""added new field on table employees

Revision ID: cd2537e78234
Revises: 9e9ed463ec93
Create Date: 2024-11-20 10:29:19.640214

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cd2537e78234'
down_revision = '9e9ed463ec93'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('employee', sa.Column('restaurant_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'employee', 'restaurants', ['restaurant_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'employee', type_='foreignkey')
    op.drop_column('employee', 'restaurant_id')
    # ### end Alembic commands ###
