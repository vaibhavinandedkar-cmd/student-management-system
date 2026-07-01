from flask import Flask

from app.config.settings import Config


def create_app():
    """
    Application Factory.
    Creates and configures the Flask application.
    """

    app = Flask(__name__)

    # Load configuration
    app.config.from_object(Config)

    # Register Routes
    from app.routes.home import home_bp
    app.register_blueprint(home_bp)

    return app
