from app_shop.shop_handler import shop_pb2
from app_shop.shop_handler import shop_pb2_grpc
from app_shop.shop_repository.shop_database import shop_db

response_text = "Shop "


class ShopServicer(shop_pb2_grpc.ShopServiceServicer):
    def Shop(self, request, context):
        response = shop_pb2.ShopResponse()
        response.message = shop_db()
        return response

