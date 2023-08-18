import grpc
from port import port

channel = grpc.insecure_channel(f'localhost:{port}')
