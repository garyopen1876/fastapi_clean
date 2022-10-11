import grpc

import grpc_pb2, grpc_pb2_grpc


def run():
    # grpc connect
    channel = grpc.insecure_channel('localhost:50054')
    stub = grpc_pb2_grpc.GreeterStub(channel)
    
    # 呼叫 server service
    response = stub.SayHello(grpc_pb2.HelloRequest(name='World'))
    print("Greeter client received: " + response.message)


if __name__ == '__main__':
    run()