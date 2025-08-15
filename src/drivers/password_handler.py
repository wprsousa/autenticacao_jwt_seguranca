import bcrypt


class PasswordHandler:
    @staticmethod
    def encrypt_password(password: str) -> str:
        salt = bcrypt.gensalt()  # elemento aleatório
        hashed_password = bcrypt.hashpw(
            password.encode("utf-8"), salt
        )  # senha + junção aleatória
        return hashed_password

    @staticmethod
    def check_password(password: str, hashed_password: str) -> bool:
        return bcrypt.checkpw(password.encode("utf-8"), hashed_password)
