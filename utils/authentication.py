import grpc
import logging

from auth_pb2_grpc import AuthenticationServiceStub
from auth_pb2 import LoginRequest, LoginResponse, RegisterRequest

from schemas.request import authentication_request as requests


def register(client: AuthenticationServiceStub, register: requests.RegisterRequest):
    req = RegisterRequest(
        username=register.username, email=register.email, password=register.password
    )
    try:
        client.Register(req)
    except grpc.RpcError as e:
        logging.error(f"Error happened while register: {e}")
        raise Exception("Error happened while register") from e


def login(client: AuthenticationServiceStub, login: requests.LoginRequest):
    req = LoginRequest(email=login.email, password=login.password)

    try:
        res: LoginResponse = client.Login(req)
        return res
    except grpc.RpcError as e:
        logging.error(f"Invalid username or password: {e}")
        raise Exception("Invalid username or password") from e
