from flask import jsonify
from app.utils.api_response import success_response
from app.utils.api_response import error_response

def success_response(
    message="Success",
    data=None,
    status_code=200
):
    """
    Standard success response.
    """

    return success_response(
    message="Student deleted successfully."
) 


def error_response(
    message="Error",
    errors=None,
    status_code=404
):
    """
    Standard error response.
    """

    return error_response(
    message="Student not found.",
    status_code=404
)
