import logging
from fastapi import APIRouter

from schemas.request.authentication_request import RegisterRequest, LoginRequest
from schemas.response.authentication_response import LoginResponse
from schemas.response.web_response import Response
from service.authentication_service import AuthenticationService

router = APIRouter(
    prefix="/authentication",
    tags=["Authentication"],
)


@router.post("/register")
def register(register_request: RegisterRequest):
    try:
        AuthenticationService().register(register_request)
        return Response(
            code=201, status="Created", message="Successfully created user!", data=None
        )
    except Exception as e:
        logging.error(f"Register failed: {e}")
        raise Exception("Cannot register") from e


@router.post("/login")
def login(login_request: LoginRequest):
    try:
        resp = AuthenticationService().login(login_request)

        return Response(
            code=200,
            status="Ok",
            message="Successfully log in!",
            data={"token": resp},
        )
    except Exception as e:
        logging.error(f"Login failed: {e}")
        raise Exception("Invalid username or password") from e
