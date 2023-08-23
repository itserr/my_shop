from app_shop.shop_proto import shop_pb2


class ShopService:
    @staticmethod
    def shop(stub, message: str):
        response = stub.Shop(shop_pb2.ShopRequest(message=message))
        return response.message
