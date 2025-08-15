from src.models.repositories.user_repository import UserRepository
from src.models.settings.db_connection_handler import db_connection_handler
from unittest.mock import Mock


class MockCursor:
    def __init__(self) -> None:
        self.execute = Mock()
        self.fetchone = Mock()


class MockConnection:
    def __init__(self) -> None:
        self.cursor = Mock(return_value=MockCursor())
        self.commit = Mock()


def test_registry_user():
    username = "fred"
    password = "Yabadabado"

    mock_connection = MockConnection()
    repo = UserRepository(mock_connection)

    repo.registry_user(username, password)

    cursor = mock_connection.cursor.return_value

    assert (
        "INSERT INTO users (username, password, balance) VALUES (?, ?, ?)"
        in cursor.execute.call_args[0][0]
    )

    assert "(username, password, balance)" in cursor.execute.call_args[0][0]

    assert "VALUES" in cursor.execute.call_args[0][0]

    assert cursor.execute.call_args[0][1] == (username, password, 0)


def test_edit_balance():
    user_id = 234
    balance = 100.11

    mock_connection = MockConnection()
    repo = UserRepository(mock_connection)

    repo.edit_balance(user_id, balance)

    cursor = mock_connection.cursor.return_value

    assert "UPDATE users" in cursor.execute.call_args[0][0]

    assert "SET balance = ?" in cursor.execute.call_args[0][0]

    assert "WHERE id = ?" in cursor.execute.call_args[0][0]

    assert cursor.execute.call_args[0][1] == (balance, user_id)

    mock_connection.commit.assert_called_once()


def test_get_user_by_username():
    user_name = "meuUsername"

    mock_connection = MockConnection()
    repo = UserRepository(mock_connection)

    repo.get_user_by_username(user_name)

    cursor = mock_connection.cursor.return_value

    assert "SELECT id, username, password" in cursor.execute.call_args[0][0]

    assert "FROM users" in cursor.execute.call_args[0][0]

    assert "username = ?" in cursor.execute.call_args[0][0]

    assert cursor.execute.call_args[0][1] == (user_name,)

    cursor.fetchone.assert_called_once()
