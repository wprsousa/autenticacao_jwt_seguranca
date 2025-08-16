from src.controllers.balance_editor import BalanceEditor


class MockUserRepository:
    def edit_balance(self, user_id: int, new_balance: float) -> None:
        pass


def test_edit():
    user_id = 10
    new_balance = 100.15

    balance_editor = BalanceEditor(MockUserRepository())
    response = balance_editor.edit(user_id, new_balance)

    assert response["type"] == "User"
    assert response["count"] == 1
    assert response["new balance"] == new_balance
