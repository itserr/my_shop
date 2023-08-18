import orders_pb2


class OrdersService:
    @staticmethod
    def orders(stub, message: str):
        response = stub.Orders(orders_pb2.OrdersRequest(message=message))
        return response.message
