from django.http import HttpResponse
from configuration.channel import channel
from app_cart.cart_handler import cart_handler
from app_cart.cart_proto import cart_pb2_grpc


def cart(request):
    stub = cart_pb2_grpc.CartServiceStub(channel)
    return HttpResponse(cart_handler.CartService.cart(stub, 'some_data_cart'))
