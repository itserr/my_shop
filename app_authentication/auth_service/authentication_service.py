from app_authentication.auth_handler import auth_pb2
from app_authentication.auth_handler import auth_pb2_grpc

response_text = "Authentication "


class AuthenticationServicer(auth_pb2_grpc.AuthenticationServiceServicer):
    def Auth(self, request, context):
        response = auth_pb2.AuthResponse()
        response.message = response_text + request.message
        return response
