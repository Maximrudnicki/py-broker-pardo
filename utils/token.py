from fastapi import HTTPException, Request


def get_token(request: Request):
    authorization_header = request.headers.get("Authorization")
    if not authorization_header:
        raise HTTPException(status_code=400, detail="Authorization header is missing")

    if not authorization_header.startswith("Bearer "):
        raise HTTPException(
            status_code=400, detail="Invalid authorization header format"
        )

    token = authorization_header[len("Bearer ") :]

    return token