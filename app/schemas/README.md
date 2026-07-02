# Schemas

## Overview

The `schemas` directory contains all data validation and serialization schemas used by the Student Management System.

Schemas define the structure of data exchanged between clients and the application. They validate incoming requests, serialize outgoing responses, and ensure that only correctly formatted data enters the business layer.

Unlike Models, Schemas do **not** represent database tables. They represent API contracts.

---

# Purpose

The purpose of the Schemas layer is to validate, transform, and serialize data flowing into and out of the application.

Schemas provide:

- Request validation
- Response serialization
- Data transformation
- Type checking
- Required field validation
- Optional field handling
- Nested object validation

They ensure that Services always receive clean, validated data.

---

# Why This Directory Exists

Without schemas:

- Routes become cluttered with validation logic.
- Services receive invalid data.
- API responses become inconsistent.
- Clients may send malformed requests.
- Validation rules are duplicated across endpoints.

Schemas centralize validation and create a consistent API contract.

---

# Responsibilities

The Schemas layer is responsible for:

- Validating incoming request payloads
- Defining API request structures
- Defining API response structures
- Serializing Python objects into JSON
- Deserializing JSON into Python objects
- Enforcing field types
- Validating required and optional fields
- Applying custom validation rules

---

# Current Directory Structure

```text
schemas/
└── README.md
```

---

# Example Future Structure

```text
schemas/
├── student_schema.py
├── department_schema.py
├── course_schema.py
├── attendance_schema.py
├── auth_schema.py
├── common_schema.py
└── README.md
```

---

# Request Flow

```text
Client JSON Request
        │
        ▼
Schema Validation
        │
        ▼
Validated Python Object
        │
        ▼
Service Layer
```

---

# Response Flow

```text
Database Model
        │
        ▼
Service
        │
        ▼
Schema Serialization
        │
        ▼
JSON Response
        │
        ▼
Client
```

---

# Position in Architecture

```text
Client

   │

Routes

   │

Schemas

   │

Services

   │

Repositories

   │

Models

   │

Database
```

Schemas sit between Routes and Services, acting as the application's validation layer.

---

# Interaction with Other Directories

Depends On

- app/models (for serialization when needed)

Used By

- routes
- services

Should Not Depend On

- repositories
- middleware

---

# Development Workflow

When creating a new API endpoint:

1. Design the request format.
2. Create a request schema.
3. Define validation rules.
4. Create a response schema.
5. Validate incoming data.
6. Pass validated data to the Service layer.
7. Serialize the response before returning it.

---

# Coding Standards

- One schema per entity.
- Separate request and response schemas.
- Use descriptive field names.
- Add field documentation.
- Apply custom validators where necessary.
- Keep schemas independent of business logic.

---

# Best Practices

- Validate all incoming data.
- Return consistent response formats.
- Reuse common schema components.
- Avoid duplicating validation rules.
- Keep serialization logic centralized.

---

# Common Mistakes

❌ Performing database queries inside schemas

❌ Embedding business logic in validation

❌ Using models directly as API payloads

❌ Skipping input validation

❌ Returning inconsistent response structures

---

# Do

- Validate every request.
- Serialize every response.
- Keep schemas reusable.
- Use custom validators where appropriate.
- Document every field.

---

# Don't

- Execute SQL queries.
- Handle HTTP requests.
- Implement business workflows.
- Access repositories directly.
- Modify database records.

---

# Example Use Case

### Request

```json
{
  "student_code": "STU001",
  "first_name": "John",
  "last_name": "Doe",
  "email": "john@example.com"
}
```

↓

Validated by:

```text
StudentCreateSchema
```

↓

Passed to:

```text
StudentService
```

---

# Performance Considerations

- Keep validation efficient.
- Reuse schema instances where possible.
- Avoid unnecessary serialization.
- Validate only required fields.

---

# Security Considerations

Schemas help protect the application by:

- Rejecting invalid input
- Preventing unexpected fields
- Enforcing data types
- Limiting payload size
- Sanitizing input where applicable

Never trust client input without schema validation.

---

# Testing Strategy

Schemas should be tested for:

- Required fields
- Optional fields
- Invalid data types
- Boundary conditions
- Custom validators
- Serialization correctness
- Deserialization correctness

---

# Dependencies

## Internal

- app/models (optional)

## External

- Marshmallow (future)
- Pydantic (future)
- Python Standard Library

---

# Related Directories

- app/routes
- app/services
- app/models

---

# References

- Marshmallow Documentation
- Pydantic Documentation
- Flask Documentation
- JSON Schema Specification

---

# FAQ

### Why not use Models directly as API objects?

Models represent database tables, while Schemas represent API contracts. Keeping them separate improves security, flexibility, and maintainability.

---

### Can a single Model have multiple Schemas?

Yes.

For example:

- StudentCreateSchema
- StudentUpdateSchema
- StudentResponseSchema
- StudentSummarySchema

Each serves a different API use case.

---

### Should validation rules be placed in Services?

Basic structural validation belongs in Schemas. Business rule validation belongs in Services.

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
