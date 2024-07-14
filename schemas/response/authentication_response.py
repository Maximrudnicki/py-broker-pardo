from pydantic import BaseModel


class LoginResponse(BaseModel):
    token_type: str
    token: str
