from flask import Blueprint, request

from app.schemas.auth_schema import LoginSchema
from app.services.auth_service import AuthService
from app.utils.api_response import (
    success_response,
    error_response
)

auth_bp = Blueprint(
    "auth",
    __name__
)

login_schema = LoginSchema()

auth_service = AuthService()


@auth_bp.route(
    "/login",
    methods=["POST"]
)
def login():

    data = request.get_json()

    errors = login_schema.validate(data)

    if errors:
        return error_response(
            message="Validation failed.",
            errors=errors,
            status_code=400
        )

    result = auth_service.login(
        username=data["username"],
        password=data["password"]
    )

    if not result:
        return error_response(
            message="Invalid username or password.",
            status_code=401
        )

    return success_response(
        message="Login successful.",
        data={
            "access_token": result["access_token"],
            "username": result["user"].username,
            "role": result["user"].role.role_name
        }
    )
