"""
Application Route Registration
"""

from .home import home_bp
from .student_routes import student_bp
from .ui_routes import erp_bp
from app.routes.auth_routes import auth_bp

def register_blueprints(app):
    """
    Register all application blueprints.
    """

    app.register_blueprint(home_bp)

    app.register_blueprint(
        student_bp,
        url_prefix="/api/v1/students"
    )

    app.register_blueprint(erp_bp)

    app.register_blueprint(
         auth_bp,
         url_prefix="/api/v1/auth"
   )
