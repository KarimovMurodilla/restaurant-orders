"""changed uniqueconstraint

Revision ID: c283224a9e44
Revises: 24c57420f568
Create Date: 2024-11-20 09:40:38.903753

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c283224a9e44'
down_revision = '24c57420f568'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('uq_user_restaurant_cart', 'carts', ['menu_item_id', 'restaurant_id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('uq_user_restaurant_cart', 'carts', type_='unique')
    # ### end Alembic commands ###
