import os


class Config:
    """
    Base configuration for the Student Management System.
    """

    # Flask Secret Key
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key")

    # Development Mode
    DEBUG = True

    # PostgreSQL Database URL
    DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://student_app:Student123@localhost:5432/student_management"
)
