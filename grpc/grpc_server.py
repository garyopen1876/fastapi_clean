import grpc
from concurrent import futures
from crud.crud_users import CRUDUser
import grpc_pb2 as grpc_pb2
import grpc_pb2_grpc as grpc_pb2_grpc
import bcrypt
from datetime import datetime, timedelta
from jose import jwt
from dotenv import load_dotenv

import os 

load_dotenv()

class Login(grpc_pb2_grpc.LoginServicer):
    def Login(self, request, _context):
        # 實現 gRPC
        db = CRUDUser()
        username = request.username
        password = request.password
        user_password = db.get_user_password(username)
        if user_password and bcrypt.checkpw(password.encode('utf8'), user_password[0][0].encode('utf8')):
            token = jwt.encode({"username": username, "exp": datetime.utcnow(
            ) + timedelta(minutes=int(os.getenv("TOKEN_LIMIT_MINUTES")))}, os.getenv("JWT_SECRET"), algorithm="HS256")
            return grpc_pb2.LoginResponse(message='Login Successfully', token=token)

        return grpc_pb2.LoginResponse(message='Login Error')


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    # 處理綁定
    grpc_pb2_grpc.add_LoginServicer_to_server(Login(), server)

    server.add_insecure_port('[::]:50054')
    server.start()
    print('gRPC server start with port 50054...')
    server.wait_for_termination()


if __name__ == '__main__':
    serve()