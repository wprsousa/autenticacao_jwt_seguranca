import pytest

from src.views.balance_editor_view import BalanceEditorView
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse


class MockController:
    @staticmethod
    def edit(user_id, new_balance):
        return {
            "type": "User",
            "count": 1,
            "new balance": new_balance
        }


def test_handle_balance_editor():
    body = {
        "new_balance": 200.15
    }

    params = {
        "user_id": 2
    }

    http_request = HttpRequest(body=body, params=params)

    mock_controller = MockController()
    balance_editor_view = BalanceEditorView(mock_controller)

    response = balance_editor_view.handle(http_request)

    assert isinstance(response, HttpResponse)
    assert response.body == {'data': {'type': 'User', 'count': 1, 'new balance': 200.15}}
    assert response.status_code == 200


def test_handle_balance_editor_with_validation_error():
    body = {}

    http_request = HttpRequest(body=body)

    mock_controller = MockController()
    user_register_view = BalanceEditorView(mock_controller)

    with pytest.raises(Exception):
        user_register_view.handle(http_request)
