from src.controllers.interfaces.balance_editor import BalanceEditorInterface
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.views.interfaces.view_interface import ViewInterface


class BalanceEditorView(ViewInterface):
    def __init__(self, controller: BalanceEditorInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        new_balance = http_request.body.get("new_balance")
        user_id = http_request.params.get("user_id")
        header_user_id = http_request.headers.get("uid")
        self.__validate_inputs(new_balance, user_id, header_user_id)

        response = self.__controller.edit(user_id, new_balance)
        return HttpResponse(body={"data": response}, status_code=200)

    @staticmethod
    def __validate_inputs(new_balance, user_id, header_user_id) -> None:
        if (
                not new_balance
                or not user_id
                or not isinstance(new_balance, float)
                or int(user_id) != int(header_user_id)
        ): raise Exception("Invalid Input")
