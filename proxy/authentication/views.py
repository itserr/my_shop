from django.shortcuts import render
from django.http import HttpResponse
from configuration.channel import channel
from app_authentication.auth_handler import auth_handler, auth_pb2_grpc


def authentication(request):
    stub = auth_pb2_grpc.AuthenticationServiceStub(channel)
    return HttpResponse(auth_handler.AuthenticationService.authentication(stub, 'some_data_auth'))
