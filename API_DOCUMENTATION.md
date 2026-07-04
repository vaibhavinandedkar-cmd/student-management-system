# API Documentation

## Base URL
```
http://localhost:5001
```

## Authentication
Currently not implemented (ready for JWT/OAuth2).

---

## Students Endpoints

### List All Students
```http
GET /api/v1/students
```

**Response**: 200 OK
```json
[
  {
    "id": 1,
    "student_code": "STU2024001",
    "first_name": "Student1",
    "last_name": "LastName1",
    "email": "student1@college.edu",
    "phone": "9880000000",
    "gender": "Male",
    "date_of_birth": "2005-05-15",
    "department_id": 1,
    "admission_date": "2023-06-01",
    "semester": 2,
    "address": "Address 1, City",
    "status": "Active",
    "created_at": "2026-07-03T12:00:00",
    "updated_at": "2026-07-03T12:00:00"
  }
]
```

### Get Student by ID
```http
GET /api/v1/students/{id}
```

**Parameters**:
- `id` (integer, required): Student ID

**Response**: 200 OK
```json
{
  "id": 1,
  "student_code": "STU2024001",
  "first_name": "Student1",
  "last_name": "LastName1",
  "email": "student1@college.edu",
  "phone": "9880000000",
  "gender": "Male",
  "date_of_birth": "2005-05-15",
  "department_id": 1,
  "admission_date": "2023-06-01",
  "semester": 2,
  "address": "Address 1, City",
  "status": "Active",
  "created_at": "2026-07-03T12:00:00",
  "updated_at": "2026-07-03T12:00:00"
}
```

### Create Student
```http
POST /api/v1/students
Content-Type: application/json
```

**Request Body**:
```json
{
  "student_code": "STU2024100",
  "first_name": "John",
  "last_name": "Doe",
  "email": "john@college.edu",
  "phone": "9876543210",
  "gender": "Male",
  "date_of_birth": "2005-05-15",
  "department_id": 1,
  "admission_date": "2023-06-01",
  "semester": 2,
  "address": "123 Main Street, City",
  "status": "Active"
}
```

**Response**: 201 Created
```json
{
  "id": 100,
  "student_code": "STU2024100",
  "first_name": "John",
  "last_name": "Doe",
  "email": "john@college.edu",
  "phone": "9876543210",
  "gender": "Male",
  "date_of_birth": "2005-05-15",
  "department_id": 1,
  "admission_date": "2023-06-01",
  "semester": 2,
  "address": "123 Main Street, City",
  "status": "Active",
  "created_at": "2026-07-03T12:05:00",
  "updated_at": "2026-07-03T12:05:00"
}
```

### Update Student
```http
PUT /api/v1/students/{id}
Content-Type: application/json
```

**Parameters**:
- `id` (integer, required): Student ID

**Request Body**: (same as create, any fields can be updated)

**Response**: 200 OK

### Delete Student
```http
DELETE /api/v1/students/{id}
```

**Parameters**:
- `id` (integer, required): Student ID

**Response**: 204 No Content

---

## Error Responses

### 400 Bad Request
```json
{
  "error": "Invalid request data",
  "details": "Field 'email' is required"
}
```

### 404 Not Found
```json
{
  "error": "Resource not found",
  "details": "Student with ID 999 not found"
}
```

### 500 Internal Server Error
```json
{
  "error": "Internal server error",
  "details": "Database connection failed"
}
```

---

## HTTP Status Codes

| Code | Meaning |
|------|---------|
| 200 | OK - Request successful |
| 201 | Created - Resource created successfully |
| 204 | No Content - Request successful (no body) |
| 400 | Bad Request - Invalid request data |
| 404 | Not Found - Resource not found |
| 500 | Internal Server Error - Server error |

---

## Example Requests

### Using cURL

**Get all students**:
```bash
curl http://localhost:5001/api/v1/students
```

**Get specific student**:
```bash
curl http://localhost:5001/api/v1/students/1
```

**Create new student**:
```bash
curl -X POST http://localhost:5001/api/v1/students \
  -H "Content-Type: application/json" \
  -d '{
    "student_code": "STU2024100",
    "first_name": "John",
    "last_name": "Doe",
    "email": "john@college.edu",
    "phone": "9876543210",
    "gender": "Male",
    "date_of_birth": "2005-05-15",
    "department_id": 1,
    "admission_date": "2023-06-01",
    "semester": 2,
    "address": "123 Main Street",
    "status": "Active"
  }'
```

**Delete student**:
```bash
curl -X DELETE http://localhost:5001/api/v1/students/1
```

### Using Python Requests

```python
import requests

BASE_URL = "http://localhost:5001"

# Get all students
response = requests.get(f"{BASE_URL}/api/v1/students")
students = response.json()

# Create student
data = {
    "student_code": "STU2024100",
    "first_name": "John",
    "last_name": "Doe",
    "email": "john@college.edu",
    "phone": "9876543210",
    "gender": "Male",
    "date_of_birth": "2005-05-15",
    "department_id": 1,
    "admission_date": "2023-06-01",
    "semester": 2,
    "address": "123 Main Street",
    "status": "Active"
}
response = requests.post(f"{BASE_URL}/api/v1/students", json=data)
new_student = response.json()
```

---

## Data Validation

### Student Fields

| Field | Type | Required | Format |
|-------|------|----------|--------|
| student_code | String | Yes | Unique, e.g., "STU2024001" |
| first_name | String | Yes | 1-100 characters |
| last_name | String | Yes | 1-100 characters |
| email | String | Yes | Valid email format, unique |
| phone | String | No | 1-15 characters |
| gender | String | No | "Male", "Female", etc. |
| date_of_birth | Date | No | YYYY-MM-DD format |
| department_id | Integer | Yes | Valid department ID |
| admission_date | Date | No | YYYY-MM-DD format |
| semester | Integer | No | 1-8 |
| address | String | No | Text |
| status | String | No | "Active", "Inactive", etc. |

---

## Pagination (Future)

```http
GET /api/v1/students?page=1&per_page=10
```

**Response Headers**:
```
X-Total-Count: 100
X-Page: 1
X-Per-Page: 10
```

---

## Filtering (Future)

```http
GET /api/v1/students?department_id=1&status=Active&semester=2
```

---

## Sorting (Future)

```http
GET /api/v1/students?sort=first_name&order=asc
```

---

## Rate Limiting (Future)

```
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 99
X-RateLimit-Reset: 1620000000
```

---

## API Versioning

Current version: **v1**

Future versions will be available at:
- `/api/v2/students`
- `/api/v3/students`

---

## Related Endpoints

Other modules follow similar REST patterns:

- `/api/v1/departments`
- `/api/v1/faculty`
- `/api/v1/courses`
- `/api/v1/subjects`
- `/api/v1/attendance`
- `/api/v1/exams`
- `/api/v1/marks`
- `/api/v1/fees`
- `/api/v1/payments`
- `/api/v1/users`
- `/api/v1/roles`

---

## Testing API

### Postman Collection

Import the following into Postman:

```json
{
  "info": {
    "name": "Student Management ERP",
    "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
  },
  "item": [
    {
      "name": "Students",
      "item": [
        {
          "name": "Get All Students",
          "request": {
            "method": "GET",
            "url": "{{base_url}}/api/v1/students"
          }
        },
        {
          "name": "Get Student",
          "request": {
            "method": "GET",
            "url": "{{base_url}}/api/v1/students/1"
          }
        },
        {
          "name": "Create Student",
          "request": {
            "method": "POST",
            "url": "{{base_url}}/api/v1/students",
            "body": {
              "mode": "raw",
              "raw": "..."
            }
          }
        }
      ]
    }
  ],
  "variable": [
    {
      "key": "base_url",
      "value": "http://localhost:5001"
    }
  ]
}
```

---

## Support

For API issues or questions, refer to:
- README.md
- DEPLOYMENT.md
- Source code in `app/routes/`

---

**Last Updated**: 2026-07-03
**Version**: 1.0.0
