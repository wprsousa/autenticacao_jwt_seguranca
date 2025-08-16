import pytest
from src.drivers.password_handler import PasswordHandler
from src.controllers.login_creator import LoginCreator

username = "meuUsername"
password = "minhaSenha"
hashed_password = PasswordHandler().encrypt_password(password)


class MockRepository:
    @staticmethod
    def get_user_by_username(username):
        return 10, username, hashed_password


def test_login_create():
    login_creator = LoginCreator(MockRepository())
    response = login_creator.create(username, password)

    assert response["access"] == True
    assert response["username"] == username
    assert response["token"] is not None


def test_login_create_wrong_password():
    login_creator = LoginCreator(MockRepository())

    with pytest.raises(Exception):
        response = login_creator.create(username, "wrongPassword")
