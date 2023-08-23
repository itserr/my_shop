from app_shop.shop_proto import shop_pb2, shop_pb2_grpc
from app_shop.shop_repository.shop_database import shop_db
from app_cart.cart_repository.cart_database import cart_db

response_text = "Shop "


class ShopServicer(shop_pb2_grpc.ShopServiceServicer):
    def Shop(self, request, context):
        response = shop_pb2.ShopResponse()
        if request.message == 'some_data_shop':
            response.message = shop_db()
        else:
            response.message = cart_db(request)
        return response

