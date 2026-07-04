#!/usr/bin/env python3
"""
Seed database with initial data for testing.
"""
from app import create_app, db
from app.models import (
    Department, Faculty, Course, Subject, Student, Role, User,
    Attendance, Exam, Mark, Fee, Payment, Notification, AuditLog
)
from datetime import datetime, date, timedelta
import random

def seed_database():
    """Populate database with sample data."""
    app = create_app()
    
    with app.app_context():
        try:
            # Check if data already exists
            if Department.query.first():
                print("⚠️  Database already contains data. Skipping seed.")
                return True
            
            print("🌱 Seeding database with initial data...")
            
            # 1. Create Departments
            departments = [
                Department(department_code="CS", department_name="Computer Science", 
                          hod_name="Dr. John Smith", status="Active"),
                Department(department_code="IT", department_name="Information Technology",
                          hod_name="Dr. Sarah Johnson", status="Active"),
                Department(department_code="EN", department_name="Engineering",
                          hod_name="Dr. Michael Brown", status="Active"),
            ]
            db.session.add_all(departments)
            db.session.commit()
            print("✓ Created 3 departments")
            
            # 2. Create Roles
            roles = [
                Role(role_name="Admin", description="System Administrator"),
                Role(role_name="Faculty", description="Faculty Member"),
                Role(role_name="Student", description="Student"),
            ]
            db.session.add_all(roles)
            db.session.commit()
            print("✓ Created 3 roles")
            
            # 3. Create Faculty
            faculty_members = [
                Faculty(faculty_code="FAC001", first_name="Dr. James",
                       last_name="Wilson", email="james.wilson@college.edu",
                       phone="9876543210", gender="Male", designation="Professor",
                       department_id=departments[0].id, joining_date=date(2015, 6, 1),
                       salary=75000, status="Active"),
                Faculty(faculty_code="FAC002", first_name="Dr. Emily",
                       last_name="Davis", email="emily.davis@college.edu",
                       phone="9876543211", gender="Female", designation="Associate Professor",
                       department_id=departments[1].id, joining_date=date(2018, 7, 15),
                       salary=65000, status="Active"),
            ]
            db.session.add_all(faculty_members)
            db.session.commit()
            print("✓ Created 2 faculty members")
            
            # 4. Create Courses
            courses = [
                Course(course_code="CS101", course_name="B.Tech Computer Science",
                      department_id=departments[0].id, duration_years=4,
                      total_semesters=8, status="Active"),
                Course(course_code="IT101", course_name="B.Tech Information Technology",
                      department_id=departments[1].id, duration_years=4,
                      total_semesters=8, status="Active"),
            ]
            db.session.add_all(courses)
            db.session.commit()
            print("✓ Created 2 courses")
            
            # 5. Create Subjects
            subjects = [
                Subject(subject_code="CS201", subject_name="Data Structures",
                       course_id=courses[0].id, semester=2, credits=4,
                       faculty_id=faculty_members[0].id),
                Subject(subject_code="CS202", subject_name="Database Systems",
                       course_id=courses[0].id, semester=3, credits=4,
                       faculty_id=faculty_members[0].id),
                Subject(subject_code="IT201", subject_name="Web Development",
                       course_id=courses[1].id, semester=2, credits=4,
                       faculty_id=faculty_members[1].id),
            ]
            db.session.add_all(subjects)
            db.session.commit()
            print("✓ Created 3 subjects")
            
            # 6. Create Students
            students = []
            for i in range(5):
                student = Student(
                    student_code=f"STU{2024001+i}",
                    first_name=f"Student{i+1}",
                    last_name=f"LastName{i+1}",
                    email=f"student{i+1}@college.edu",
                    phone=f"988000000{i}",
                    gender=random.choice(["Male", "Female"]),
                    date_of_birth=date(2005, random.randint(1,12), random.randint(1,28)),
                    department_id=departments[0].id,
                    admission_date=date(2023, 6, 1),
                    semester=2,
                    address=f"Address {i+1}, City",
                    status="Active"
                )
                students.append(student)
            db.session.add_all(students)
            db.session.commit()
            print(f"✓ Created {len(students)} students")
            
            # 7. Create Users
            users = [
                User(username="admin", email="admin@college.edu", 
                    password_hash="admin123", role_id=roles[0].id, is_active=True),
                User(username="faculty1", email="faculty1@college.edu",
                    password_hash="fac123", role_id=roles[1].id, is_active=True),
            ]
            db.session.add_all(users)
            db.session.commit()
            print("✓ Created 2 users")
            
            # 8. Create Notifications
            notifications = [
                Notification(title="Welcome", message="Welcome to Student Management System",
                           notification_type="system", status="Active"),
                Notification(title="Exam Scheduled", message="Mid-term exams scheduled for next week",
                           notification_type="academic", status="Active"),
            ]
            db.session.add_all(notifications)
            db.session.commit()
            print("✓ Created 2 notifications")
            
            # 9. Create Fees
            fees = [
                Fee(student_id=students[0].id, fee_type="Tuition",
                   amount=50000, academic_year="2024-2025", due_date=date(2024, 7, 31),
                   status="Pending"),
                Fee(student_id=students[1].id, fee_type="Hostel",
                   amount=30000, academic_year="2024-2025", due_date=date(2024, 7, 31),
                   status="Pending"),
            ]
            db.session.add_all(fees)
            db.session.commit()
            print("✓ Created 2 fees")
            
            print("\n✅ Database seeding completed successfully!")
            return True
            
        except Exception as e:
            print(f"❌ Error seeding database: {e}")
            db.session.rollback()
            return False

if __name__ == '__main__':
    import sys
    success = seed_database()
    sys.exit(0 if success else 1)
