from app_cart.cart_proto import cart_pb2


class CartService:
    @staticmethod
    def cart(stub, message: str):
        response = stub.Cart(cart_pb2.CartRequest(message=message))
        return response.message
