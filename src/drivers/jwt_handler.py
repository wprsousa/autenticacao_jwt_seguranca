import jwt
from datetime import datetime, timedelta, timezone
from src.configs.jwt_configs import jwt_infos


class JwtHandler:
    @staticmethod
    def create_jwt_token(body=None) -> str:
        if body is None:
            body = {}
        token = jwt.encode(
            payload={"exp": datetime.now(timezone.utc) + timedelta(hours=int(jwt_infos["JWT_HOURS"])), **body, },
            key=jwt_infos["KEY"],
            algorithm=jwt_infos["ALGORITHM"],
        )
        return token

    @staticmethod
    def decode_jwt_token(token: str) -> dict:
        token_information = jwt.decode(
            token, key=jwt_infos["KEY"], algorithms=jwt_infos["ALGORITHM"]
        )
        return token_information
