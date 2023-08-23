from app_orders.orders_proto import orders_pb2, orders_pb2_grpc

response_text = "Orders "


class OrdersServicer(orders_pb2_grpc.OrdersServiceServicer):
    def Orders(self, request, context):
        response = orders_pb2.OrdersResponse()
        response.message = response_text + request.message
        return response
