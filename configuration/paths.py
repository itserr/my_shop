import sys

index = None

for path in sys.path:
    if path[-7:] == 'my_shop':
        index = sys.path.index(path)
        sys.path.append(sys.path[index] + "/app_authentication/auth_handler")
        sys.path.append(sys.path[index] + "/app_authentication/auth_repository")
        sys.path.append(sys.path[index] + "/app_authentication/auth_service")
        sys.path.append(sys.path[index] + "/app_cart/cart_handler")
        sys.path.append(sys.path[index] + "/app_cart/cart_repository")
        sys.path.append(sys.path[index] + "/app_cart/cart_service")
        sys.path.append(sys.path[index] + "/app_orders/orders_handler")
        sys.path.append(sys.path[index] + "/app_orders/orders_repository")
        sys.path.append(sys.path[index] + "/app_orders/orders_service")
        sys.path.append(sys.path[index] + "/app_shop/shop_handler")
        sys.path.append(sys.path[index] + "/app_shop/shop_repository")
        sys.path.append(sys.path[index] + "/app_shop/shop_service")
        sys.path.append(sys.path[index] + "/configuration")
        sys.path.append(sys.path[index] + "/server")
        break
