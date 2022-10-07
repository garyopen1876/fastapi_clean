import grpc
from concurrent import futures
import grpc_pb2
import grpc_pb2_grpc


# 實現 proto 定義的方法 
class Greeter(grpc_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        # 要處理的事情
        return grpc_pb2.HelloResponse(message='Hello {msg}'.format(msg=request.name))


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    # 處理綁定
    grpc_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)

    server.add_insecure_port('[::]:50054')
    server.start()
    print('gRPC server start with port 50054...')
    server.wait_for_termination()


if __name__ == '__main__':
    serve()