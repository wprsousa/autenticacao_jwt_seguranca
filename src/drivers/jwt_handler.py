import jwt
from datetime import datetime, timedelta, timezone


class JwtHandler:
    @staticmethod
    def create_jwt_token(body=None) -> str:
        if body is None:
            body = {}
        token = jwt.encode(
            payload={"exp": datetime.now(timezone.utc) + timedelta(minutes=1), **body},
            key="minhaChave",
            algorithm="HS256",
        )
        return token

    @staticmethod
    def decode_jwt_token(token: str) -> dict:
        token_information = jwt.decode(token, key="minhaChave", algorithms="HS256")
        return token_information
