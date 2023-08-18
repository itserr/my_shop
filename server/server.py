import sys
sys.path.append(sys.path[1]+"/configuration/paths.py")
exec(open(sys.path[len(sys.path)-1]).read())

import grpc
from concurrent import futures
from app_shop.shop_handler import shop_pb2_grpc
from app_shop.shop_service import shop_service
from app_orders.orders_handler import orders_pb2_grpc
from app_orders.orders_service import orders_service
from app_cart.cart_handler import cart_pb2_grpc
from app_cart.cart_service import cart_service
from app_authentication.auth_handler import auth_pb2_grpc
from app_authentication.auth_service import authentication_service


server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
shop_pb2_grpc.add_ShopServiceServicer_to_server(shop_service.ShopServicer(), server)
orders_pb2_grpc.add_OrdersServiceServicer_to_server(orders_service.OrdersServicer(), server)
cart_pb2_grpc.add_CartServiceServicer_to_server(cart_service.CartServicer(), server)
auth_pb2_grpc.add_AuthenticationServiceServicer_to_server(authentication_service.AuthenticationServicer(), server)
server.add_insecure_port('[::]:8080')
server.start()
server.wait_for_termination()
