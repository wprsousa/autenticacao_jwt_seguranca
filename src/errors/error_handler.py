from .types.http_bad_request import HttpBadRequestError
from .types.http_not_found import HttpNotFoundError
from .types.http_unauthorized import HttpUnauthorizedError
from src.views.http_types.http_response import HttpResponse


def error_handler(error: Exception) -> HttpResponse:
    if isinstance(error, (HttpNotFoundError, HttpUnauthorizedError, HttpBadRequestError)):
        return HttpResponse(
            body={
                "errors": [
                    {
                        "title": error.name,
                        "detail": error.message
                    }
                ]
            },
            status_code=error.status_code
        )
    return HttpResponse(
        status_code=500,
        body={"errors": [{"title": "Internal Server Error", "detail": str(error)}]}
    )
