import sys

index = 0
sys_path = sys.path[index]

for path in sys.path:
    if path[-7:] == 'my_shop' or path[-5:] == 'proxy':
        if path[-5:] == 'proxy':
            sys_path = sys.path[index][:-6]
        index = sys.path.index(path)
        sys.path.append(sys_path + "/app_authentication/auth_handler")
        sys.path.append(sys_path + "/app_authentication/auth_repository")
        sys.path.append(sys_path + "/app_authentication/auth_service")
        sys.path.append(sys_path + "/app_authentication/auth_proto")
        sys.path.append(sys_path + "/app_cart/cart_handler")
        sys.path.append(sys_path + "/app_cart/cart_repository")
        sys.path.append(sys_path + "/app_cart/cart_service")
        sys.path.append(sys_path + "/app_cart/cart_proto")
        sys.path.append(sys_path + "/app_orders/orders_handler")
        sys.path.append(sys_path + "/app_orders/orders_repository")
        sys.path.append(sys_path + "/app_orders/orders_service")
        sys.path.append(sys_path + "/app_orders/orders_proto")
        sys.path.append(sys_path + "/app_shop/shop_handler")
        sys.path.append(sys_path + "/app_shop/shop_repository")
        sys.path.append(sys_path + "/app_shop/shop_service")
        sys.path.append(sys_path + "/app_shop/shop_proto")
        sys.path.append(sys_path + "/configuration")
        sys.path.append(sys_path + "/server")
        sys.path.append(sys_path + "/proxy/templates/shop/shop.html")
        break
