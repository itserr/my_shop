from app_cart.cart_proto import cart_pb2, cart_pb2_grpc

response_text = "Cart "


class CartServicer(cart_pb2_grpc.CartServiceServicer):
    def Cart(self, request, context):
        response = cart_pb2.CartResponse()
        response.message = response_text + request.message
        return response
