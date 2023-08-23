from app_authentication.auth_proto import auth_pb2


class AuthenticationService:
    @staticmethod
    def authentication(stub, message: str):
        response = stub.Auth(auth_pb2.AuthRequest(message=message))
        return response.message
