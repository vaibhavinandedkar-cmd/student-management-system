from flask import Flask

from app.config.settings import Config
from app.config.database import db, migrate


def create_app():
    """
    Application Factory.
    Creates and configures the Flask application.
    """

    app = Flask(__name__)

    # Load configuration
    app.config.from_object(Config)

    # Initialize Database
    db.init_app(app)

    # Initialize Migrations
    migrate.init_app(app, db)

    # Register Routes
    from app.routes.home import home_bp
    app.register_blueprint(home_bp)

    return app
