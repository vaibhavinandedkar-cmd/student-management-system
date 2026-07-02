"""
Application Route Registration
"""

from .home import home_bp
from .student_routes import student_bp


def register_blueprints(app):
    """
    Register all application blueprints.
    """

    app.register_blueprint(home_bp)

    app.register_blueprint(
        student_bp,
        url_prefix="/api/v1/students"
    )
