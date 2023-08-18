from django.shortcuts import render
from django.http import HttpResponse
from configuration.channel import channel
from app_orders.orders_handler import orders_handler, orders_pb2_grpc


def orders(request):
    stub = orders_pb2_grpc.OrdersServiceStub(channel)
    return HttpResponse(orders_handler.OrdersService.orders(stub, 'some_data_orders'))
