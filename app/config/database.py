from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# SQLAlchemy instance
db = SQLAlchemy()

# Flask-Migrate instance
migrate = Migrate()
