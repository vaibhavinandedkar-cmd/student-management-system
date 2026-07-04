#!/usr/bin/env python3
"""
Initialize the database schema directly using SQLAlchemy.
Bypasses Alembic to work around permission issues.
"""
import os
import sys
from app import create_app, db
from app import models  # Import all models to register them

def init_database():
    """Create all tables from models."""
    app = create_app()
    
    with app.app_context():
        try:
            print("🔧 Creating database schema...")
            db.create_all()
            print("✅ Database schema created successfully!")
            return True
        except Exception as e:
            print(f"❌ Error creating schema: {e}")
            return False

if __name__ == '__main__':
    success = init_database()
    sys.exit(0 if success else 1)
