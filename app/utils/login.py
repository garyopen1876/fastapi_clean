from app.schemas.login import LoginMessage
from app.utils.app_error import UsernamePasswordError
from app.setting import settings
from app.grpc import grpc_pb2_grpc
from app.grpc import grpc_pb2
import grpc


def login(username: str, password: str) -> LoginMessage:
    # grpc connect
    channel = grpc.insecure_channel(settings.grpc_url)
    stub = grpc_pb2_grpc.LoginStub(channel)
    # 呼叫 server service
    response = stub.Login(grpc_pb2.LoginRequest(
        username=username, password=password))
    if response.message == "Login Error":
        raise UsernamePasswordError()
    return {"message": response.message, "token": response.token}
