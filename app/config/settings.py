import os


class Config:
    """
    Base configuration for the Student Management System.
    """

    # ----------------------------------------
    # Flask Configuration
    # ----------------------------------------

    # Secret key used for sessions, cookies, CSRF protection, etc.
    SECRET_KEY = os.getenv(
        "SECRET_KEY",
        "dev-secret-key"
    )

    # Enable debug mode for development
    DEBUG = True

    # ----------------------------------------
    # Database Configuration
    # ----------------------------------------

    # SQLAlchemy looks specifically for this variable.
    # It contains the PostgreSQL connection string.
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "postgresql://student_app:Student123@localhost:5432/student_management"
    )

    # Disable SQLAlchemy modification tracking.
    # Saves memory and improves performance.
    SQLALCHEMY_TRACK_MODIFICATIONS = False
