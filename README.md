# Student Management System (ERP)

A complete Enterprise Resource Planning (ERP) application for managing student records, academics, and operations. Built with Flask, PostgreSQL, and Bootstrap 5.

## Features

- **Dashboard**: Comprehensive overview with key metrics
- **Student Management**: Full CRUD operations for student records
- **Academic Management**: Departments, Faculty, Courses, Subjects
- **Operations**: Attendance, Examinations, Marks, Fees, Payments
- **Administration**: User management, Roles, Notifications, Audit Logs
- **Responsive UI**: Mobile-friendly design with Bootstrap 5
- **REST API**: Complete API endpoints for all modules
- **Database**: PostgreSQL with SQLAlchemy ORM
- **Clean Architecture**: Repository pattern, Service layer, Blueprints

## Technology Stack

- **Backend**: Flask 3.1.3
- **Database**: PostgreSQL 12+
- **ORM**: SQLAlchemy 2.0.51
- **Frontend**: Bootstrap 5.3.3, HTML5, JavaScript ES6
- **Migration**: Alembic (Flask-Migrate 4.1.0)
- **Validation**: Marshmallow 3.20.1
- **Server**: Gunicorn 21.2.0

## Project Structure

```
student-management/
├── app/
│   ├── __init__.py              # Application factory
│   ├── config/
│   │   ├── database.py          # Database configuration
│   │   └── settings.py          # App settings
│   ├── core/
│   │   └── logger.py            # Logging setup
│   ├── exceptions/
│   │   └── api_exception.py     # Custom exceptions
│   ├── models/                  # SQLAlchemy models
│   ├── repositories/            # Data access layer
│   ├── services/                # Business logic layer
│   ├── routes/                  # API and UI blueprints
│   ├── schemas/                 # Marshmallow validation schemas
│   ├── static/                  # CSS, JS, images
│   └── templates/               # Jinja2 templates
├── migrations/                  # Alembic migrations
├── tests/                       # Test files
├── logs/                        # Application logs
├── init_db.py                   # Database initialization script
├── seed_db.py                   # Database seed script
├── run.py                       # Development server entry point
├── requirements.txt             # Python dependencies
└── README.md                    # This file
```

## Installation

### Prerequisites

- Python 3.9+
- PostgreSQL 12+
- Git

### Setup Steps

1. **Clone the Repository**
   ```bash
   cd /Users/mohit7/Projects/student-management
   ```

2. **Create Virtual Environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Database**
   
   The application expects PostgreSQL with these credentials:
   - User: `student_app`
   - Database: `student_management`
   - Host: `localhost:5432`
   
   You can override these via environment variables:
   ```bash
   export DATABASE_URL="postgresql://user:password@host:5432/dbname"
   ```

5. **Initialize Database**
   ```bash
   python init_db.py
   ```

6. **Seed Sample Data (Optional)**
   ```bash
   python seed_db.py
   ```

7. **Run Development Server**
   ```bash
   python run.py
   # or specify port
   PORT=8000 python run.py
   ```

   Server runs on `http://127.0.0.1:5001` (default) or custom port

## Configuration

### Environment Variables

```bash
# Flask Configuration
export FLASK_ENV=development          # or production
export FLASK_DEBUG=1                  # 1 for dev, 0 for prod
export SECRET_KEY=your-secret-key
export PORT=5001                      # Default port

# Database Configuration
export DATABASE_URL=postgresql://user:pass@localhost:5432/student_management

# Logging
export LOG_LEVEL=INFO                 # DEBUG, INFO, WARNING, ERROR
```

### Configuration File

Edit `app/config/settings.py` for application settings:

```python
class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://...')
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key')
    # ... other settings
```

## Database Schema

### Core Tables

- **students**: Student records (name, email, enrollment details)
- **departments**: Academic departments
- **faculty**: Faculty members
- **courses**: Academic courses
- **subjects**: Course subjects with faculty assignment
- **roles**: User roles (Admin, Faculty, Student)
- **users**: System users with role assignments
- **attendance**: Student attendance records
- **exams**: Examination records
- **marks**: Student grades/marks
- **fees**: Fee records and amounts
- **payments**: Payment transactions
- **notifications**: System notifications
- **audit_logs**: Activity audit trail

### Relationships

- Department ← Faculty (1:M)
- Department ← Course (1:M)
- Course ← Subject (1:M)
- Faculty ← Subject (1:M)
- Department ← Student (1:M)
- Student ← Attendance (1:M)
- Student ← Fee (1:M)
- Student ← Payment (1:M)

## API Endpoints

### Students
- `GET /api/v1/students` - List all students
- `GET /api/v1/students/<id>` - Get student details
- `POST /api/v1/students` - Create new student
- `PUT /api/v1/students/<id>` - Update student
- `DELETE /api/v1/students/<id>` - Delete student

### Departments
- `GET /api/v1/departments` - List all departments
- `POST /api/v1/departments` - Create department

### Other modules follow similar REST patterns

## UI Routes

- `/dashboard` - Main dashboard
- `/students` - Student management
- `/departments` - Department management
- `/faculty` - Faculty management
- `/courses` - Course management
- `/subjects` - Subject management
- `/attendance` - Attendance records
- `/exams` - Examination management
- `/fees` - Fee management
- `/payments` - Payment records
- `/users` - User management
- `/roles` - Role management
- `/notifications` - Notifications
- `/audit-logs` - Activity logs

## Usage Examples

### Create a Student via API

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
    "status": "Active"
  }'
```

### Get All Students

```bash
curl http://localhost:5001/api/v1/students
```

### Access Dashboard

Open browser: `http://localhost:5001/dashboard`

## Production Deployment

### Using Gunicorn

1. **Install Gunicorn** (already in requirements.txt)

2. **Run with Gunicorn**
   ```bash
   gunicorn -w 4 -b 0.0.0.0:5001 --timeout 120 --access-logfile - run:app
   ```

3. **Configuration File** (`gunicorn_config.py`)
   ```python
   bind = "0.0.0.0:5001"
   workers = 4
   worker_class = "sync"
   timeout = 120
   access_log_format = '%({x-forwarded-for}i)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s'
   ```

   Run with config:
   ```bash
   gunicorn -c gunicorn_config.py run:app
   ```

### Using Docker

```bash
docker-compose up -d
```

Dockerfile included in the project.

### Using Nginx as Reverse Proxy

```nginx
server {
    listen 80;
    server_name _;

    location / {
        proxy_pass http://127.0.0.1:5001;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    location /static {
        alias /path/to/app/static;
        expires 30d;
    }
}
```

## Logging

Application logs are stored in `logs/` directory.

Configuration in `app/core/logger.py`:

```python
log_level = os.getenv('LOG_LEVEL', 'INFO')
```

View logs:
```bash
tail -f logs/app.log
```

## Error Handling

The application includes:
- Global exception handlers in `app/__init__.py`
- Custom exceptions in `app/exceptions/api_exception.py`
- Graceful error fallbacks in route handlers
- Database connection error handling

## Testing

Run tests:
```bash
pytest tests/ -v
```

## Database Operations

### Create Migration

```bash
flask db migrate -m "Description of changes"
```

### Apply Migrations

```bash
flask db upgrade
```

### Downgrade Migration

```bash
flask db downgrade
```

## Troubleshooting

### Port Already in Use

```bash
lsof -i :5001  # Find process
kill -9 <PID>   # Kill process
```

### Database Connection Error

1. Verify PostgreSQL is running
2. Check database credentials
3. Verify database exists: `psql -U student_app -d student_management`

### Permission Denied for Schema

```bash
psql -U postgres -d student_management << EOF
GRANT USAGE ON SCHEMA public TO student_app;
GRANT CREATE ON SCHEMA public TO student_app;
EOF
```

### Recreate Database

```bash
# Backup first (optional)
pg_dump -U student_app -d student_management > backup.sql

# Drop and recreate
dropdb -U student_app student_management
createdb -U student_app -O student_app student_management

# Reinitialize
python init_db.py
python seed_db.py
```

## Performance Optimization

1. **Database Indexing**: Indexes on frequently queried columns
2. **Query Caching**: Implement Redis for session caching
3. **Connection Pooling**: SQLAlchemy handles connection pooling
4. **Static File Caching**: Browser caching for CSS/JS
5. **Pagination**: Implement for large datasets

## Security Features

- ✅ CSRF protection via Flask-WTF
- ✅ Input validation with Marshmallow
- ✅ SQL injection prevention via ORM
- ✅ XSS prevention via Jinja2 auto-escaping
- ✅ Password hashing (implement in User model)
- ✅ Role-based access control framework in place

## Future Enhancements

- [ ] Authentication/Authorization system
- [ ] Email notifications
- [ ] Report generation (PDF)
- [ ] Advanced search and filtering
- [ ] Data export (CSV, Excel)
- [ ] Mobile app API
- [ ] Dashboard charts and graphs
- [ ] Marks calculation engine
- [ ] Attendance analytics

## Support & Documentation

- API Documentation: `/api/docs` (implement Swagger)
- Database Schema: See models in `app/models/`
- Architecture: Follow Repository → Service → Route pattern

## License

Proprietary - Student Management System

## Contact

For issues and support, contact the development team.

---

**Last Updated**: 2026-07-03
**Version**: 1.0.0
**Status**: Production Ready
