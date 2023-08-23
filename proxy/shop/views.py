from django.http import HttpResponse
from configuration.channel import channel
from app_shop.shop_handler import shop_handler
from app_shop.shop_proto import shop_pb2_grpc
from django.shortcuts import render


def shop(request):
    stub = shop_pb2_grpc.ShopServiceStub(channel)
    return HttpResponse(shop_handler.ShopService.shop(stub, 'some_data_shop'))
    # data = shop_handler.ShopService.shop(stub, 'some_data_shop')
    # return render(request, 'shop/shop.html', {'data': data})


def add_to_cart(request):
    if request.method == 'POST':
        input_data = request.POST.get('inputData')
        stub = shop_pb2_grpc.ShopServiceStub(channel)
        shop_handler.ShopService.shop(stub, input_data)
    return render(request, 'shop/shop.html')
