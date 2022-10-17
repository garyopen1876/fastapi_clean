from app.schemas.login import LoginMessage
from app.utils.app_error import UsernamePasswordError
from app.utils import grpc_pb2_grpc
from app.utils import grpc_pb2

import grpc


def login(username: str, password: str) -> LoginMessage:
    # grpc connect
    channel = grpc.insecure_channel('localhost:50054')
    stub = grpc_pb2_grpc.LoginStub(channel)

    # 呼叫 server service
    response = stub.Login(grpc_pb2.LoginRequest(
        username=username, password=password))

    return {"response": response}
