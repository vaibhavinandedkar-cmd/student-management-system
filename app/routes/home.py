from flask import Blueprint

home_bp = Blueprint("home", __name__)


@home_bp.route("/")
def home():
    return {
        "application": "Student Management System",
        "status": "Running",
        "version": "1.0.0"
    }
