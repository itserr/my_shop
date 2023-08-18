from django.http import HttpResponse
from django.shortcuts import render
from configuration.channel import channel
from app_shop.shop_handler import shop_handler, shop_pb2_grpc


def shop(request):
    stub = shop_pb2_grpc.ShopServiceStub(channel)
    return HttpResponse(shop_handler.ShopService.shop(stub, 'some_data_shop'))
