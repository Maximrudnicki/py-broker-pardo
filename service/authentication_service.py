import logging
import grpc

from auth_pb2_grpc import AuthenticationServiceStub

from schemas.request import authentication_request as requests
from utils.authentication import login, register

from config.config import AUTH_SERVICE


class AuthenticationService:
    def connect_to_auth_service(self):
        try:
            return grpc.insecure_channel(AUTH_SERVICE)
        except Exception as e:
            logging.error(f"Failed to connect to auth service: {e}")
            raise Exception("Failed to connect to auth service") from e

    def register(self, user: requests.RegisterRequest):
        with self.connect_to_auth_service() as channel:
            client = AuthenticationServiceStub(channel)
            try:
                register(client, user)
            except Exception as e:
                logging.error(f"Register failed: {e}")
                raise Exception("Cannot register") from e

    def login(self, user: requests.LoginRequest):
        with self.connect_to_auth_service() as channel:
            client = AuthenticationServiceStub(channel)
            try:
                login_response = login(client, user)
                return login_response.token
            except Exception as e:
                logging.error(f"Login failed: {e}")
                raise Exception("Invalid username or password") from e
