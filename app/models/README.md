# Models

## Overview

The `models` directory contains the database models of the Student Management System.

A model represents a real-world business entity and defines how that entity is stored in the database using SQLAlchemy's Object Relational Mapper (ORM).

Models serve as the bridge between Python objects and relational database tables.

Every table in the database should have a corresponding model class.

---

# Purpose

The purpose of the Models layer is to define the application's data structure.

It specifies:

- Database tables
- Columns
- Data types
- Constraints
- Relationships
- Primary keys
- Foreign keys
- Default values
- Indexes

The Models layer represents **what data exists**, not **how it is processed**.

---

# Why This Directory Exists

Separating models from business logic ensures:

- Clean architecture
- Reusable data definitions
- Easier database migrations
- Consistent ORM mapping
- Better maintainability
- Simplified testing

Models should remain focused on representing data rather than implementing business workflows.

---

# Responsibilities

The Models layer is responsible for:

- Defining database tables
- Mapping Python classes to database tables
- Defining column types
- Declaring primary keys
- Defining foreign keys
- Managing relationships
- Applying database constraints
- Providing ORM mappings
- Supporting database migrations

---

# Current Directory Structure

```text
models/
├── student.py
└── README.md
```

---

# Example Future Structure

```text
models/
├── student.py
├── course.py
├── faculty.py
├── department.py
├── attendance.py
├── subject.py
├── examination.py
├── marks.py
├── user.py
├── role.py
├── permission.py
└── README.md
```

Each model should represent a single business entity.

---

# Model Example

```python
class Student(db.Model):
    __tablename__ = "students"

    id = db.Column(db.Integer, primary_key=True)

    student_code = db.Column(db.String(20), unique=True)

    first_name = db.Column(db.String(100))

    email = db.Column(db.String(120), unique=True)
```

The ORM automatically maps this Python class to a database table.

---

# Database Mapping

```text
Student Class
        │
        ▼
SQLAlchemy ORM
        │
        ▼
students Table
        │
        ▼
PostgreSQL
```

---

# Position in Architecture

```text
Routes

    │

Services

    │

Repositories

    │

Models

    │

PostgreSQL
```

Models represent the database schema and are accessed through repositories.

---

# Interaction with Other Directories

Used By

- repositories
- migrations
- services (indirectly)

Depends On

- app/extensions
- SQLAlchemy

Should Not Depend On

- routes
- services
- middleware

Models should remain independent of application workflows.

---

# Development Workflow

When creating a new model:

1. Identify the business entity.
2. Create a model class.
3. Define the table name.
4. Add columns.
5. Define relationships.
6. Add constraints.
7. Generate Alembic migration.
8. Apply migration.
9. Write unit tests.
10. Update documentation.

---

# Coding Standards

- One model per file.
- Use singular class names.
- Use plural table names.
- Define explicit column types.
- Use meaningful names.
- Add docstrings.
- Include timestamps where appropriate.
- Follow PEP 8.

---

# Best Practices

- Keep models simple.
- Normalize database design.
- Use relationships instead of duplicate data.
- Define indexes where necessary.
- Prefer ORM relationships over manual joins.
- Keep business logic outside models.

---

# Common Mistakes

❌ Writing business logic inside models

❌ Executing database queries in models

❌ Creating circular relationships

❌ Using inconsistent naming

❌ Forgetting indexes

❌ Missing constraints

---

# Do

- Represent business entities.
- Define relationships clearly.
- Keep models reusable.
- Document every field.
- Use migrations for schema changes.

---

# Don't

- Write API logic.
- Perform database queries.
- Implement business workflows.
- Access HTTP requests.
- Handle authentication.

---

# Relationships

Typical SQLAlchemy relationships include:

- One-to-One
- One-to-Many
- Many-to-One
- Many-to-Many

Example:

```python
department = db.relationship(
    "Department",
    back_populates="students"
)
```

Relationships simplify navigation between related entities.

---

# Performance Considerations

When designing models:

- Add indexes to frequently queried columns.
- Avoid unnecessary relationships.
- Use lazy loading appropriately.
- Normalize data.
- Prevent N+1 query issues.

Proper model design has a significant impact on application performance.

---

# Security Considerations

Models should never store:

- Plain-text passwords
- Secrets
- API keys
- Sensitive tokens

Sensitive information should be encrypted or hashed before storage.

---

# Testing Strategy

Models should be tested for:

- Constraints
- Relationships
- Default values
- Unique indexes
- Foreign keys
- Validation behavior
- ORM mappings

---

# Dependencies

## Internal

- app/extensions

## External

- SQLAlchemy
- Flask-SQLAlchemy
- Alembic

---

# Related Directories

- app/repositories
- app/services
- migrations
- database/sql

---

# References

- SQLAlchemy ORM Documentation
- Flask-SQLAlchemy Documentation
- PostgreSQL Documentation
- Alembic Documentation

---

# FAQ

### Should business logic be placed in models?

No.

Models should describe the database structure only. Business rules belong in the Services layer.

---

### Why use one model per file?

It improves readability, maintainability, version control, and testing.

---

### Can models contain helper methods?

Yes, lightweight helper methods are acceptable, but complex workflows should remain in Services.

---

# AI Development Notes

| Item | Value |
|------|-------|
| Generated By | ChatGPT / Gemini |
| Reviewed By | Developer |
| Documentation Version | 1.0 |

---

# Revision History

| Version | Description |
|---------|-------------|
| 1.0 | Initial documentation |
