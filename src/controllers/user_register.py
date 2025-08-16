from src.controllers.interfaces.user_register import UserRegisterInterface
from src.drivers.password_handler import PasswordHandler
from src.models.interface.user_repository import UserRepositoryInterface

class UserRegister(UserRegisterInterface):
    def __init__(self, user_repository: UserRepositoryInterface) -> None:
        self.__user_repository = user_repository
        self.__password_handle = PasswordHandler()

    def registry(self, username: str, password: str) -> dict:
        hashed_password = self.__create_hash_password(password)
        self.__registry_new_user(username, hashed_password)
        return self.__format_response(username)

    def __create_hash_password(self, password: str) -> str:
        hashed_password = self.__password_handle.encrypt_password(password)
        return hashed_password

    def __registry_new_user(self, username: str, hashed_password: str) -> None:
        self.__user_repository.registry_user(username, hashed_password)

    @staticmethod
    def __format_response(username: str) -> dict:
        return {"type": "User", "count": 1, "username": username}
