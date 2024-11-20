from api.auth_user import router_jwt, router_auth
from api.users import router as router_user
from api.menu_item import router as router_menu_item
from api.restaurant import router as router_restaurant
from api.cart import router as router_cart
from api.employee import router as router_employee

all_routers = [
    router_jwt,
    router_auth,

    router_user,
    router_menu_item,
    router_restaurant,
    router_cart,
    router_employee,
]
