from datetime import date

from flask import Blueprint, flash, redirect, render_template, request, url_for
from marshmallow import ValidationError

import app.models
from app.models.student import Student
from app.schemas.erp_schema import (
    CourseFormSchema,
    DepartmentFormSchema,
    FacultyFormSchema,
    StudentFormSchema,
    SubjectFormSchema,
)
from app.services.attendance_service import AttendanceService
from app.services.course_service import CourseService
from app.services.department_service import DepartmentService
from app.services.exam_service import ExamService
from app.services.fee_service import FeeService
from app.services.faculty_service import FacultyService
from app.services.notification_service import NotificationService
from app.services.payment_service import PaymentService
from app.services.role_service import RoleService
from app.services.student_service import StudentService
from app.services.subject_service import SubjectService
from app.services.user_service import UserService
from app.services.audit_log_service import AuditLogService

erp_bp = Blueprint("erp", __name__)

student_service = StudentService()
department_service = DepartmentService()
faculty_service = FacultyService()
course_service = CourseService()
subject_service = SubjectService()
attendance_service = AttendanceService()
exam_service = ExamService()
fee_service = FeeService()
payment_service = PaymentService()
user_service = UserService()
role_service = RoleService()
notification_service = NotificationService()
audit_log_service = AuditLogService()

student_schema = StudentFormSchema()
department_schema = DepartmentFormSchema()
faculty_schema = FacultyFormSchema()
course_schema = CourseFormSchema()
subject_schema = SubjectFormSchema()

STATUS_OPTIONS = ["Active", "Inactive", "Pending", "On Leave"]


def safe_get_all(service_fn, fallback=None, error_msg=None):
    """
    Safely call a service.get_all() and return empty list on DB errors.
    If error_msg is provided, flash it as a warning.
    """
    try:
        return service_fn()
    except Exception as e:
        if error_msg:
            flash(error_msg, 'warning')
        return fallback or []


def safe_route(func):
    """
    Decorator to wrap route handlers and catch all database errors.
    Shows warning toast but allows page to render.
    """
    from functools import wraps
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            flash(f'Database connection issue. Please try again.', 'warning')
            # Continue rendering the page with empty data
            return render_template("error.html", error=str(e))
    return wrapper


@erp_bp.app_context_processor
def inject_current_year():
    return {
        "current_year": date.today().year
    }


@erp_bp.route("/dashboard")
def dashboard():
    try:
        students = student_service.get_all()
        faculty = faculty_service.get_all()
        departments = department_service.get_all()
        courses = course_service.get_all()
        attendance_records = attendance_service.get_all()
        fees = fee_service.get_all()
        exams = exam_service.get_all()
        notifications = notification_service.get_all()
        audit_logs = audit_log_service.get_all()
    except Exception as e:
        # If the DB schema is not in sync, show the dashboard with empty data
        flash('Some dashboard data could not be loaded: {}'.format(str(e)), 'warning')
        students = faculty = departments = courses = attendance_records = fees = exams = notifications = audit_logs = []

    today_attendance = sum(
        1 for attendance in attendance_records
        if attendance.attendance_date == date.today()
    )
    pending_fees = sum(
        1 for fee in fees
        if fee.status and fee.status.lower() == "pending"
    )
    upcoming_exams = [
        exam for exam in exams
        if exam.exam_date and exam.exam_date >= date.today()
    ]

    return render_template(
        "dashboard.html",
        active_page="dashboard",
        stats={
            "students": len(students),
            "faculty": len(faculty),
            "departments": len(departments),
            "courses": len(courses),
            "today_attendance": today_attendance,
            "pending_fees": pending_fees,
            "upcoming_exams": len(upcoming_exams),
        },
        recent_notifications=notifications[-5:],
        latest_activities=audit_logs[-5:],
        quick_actions=[
            {"label": "New Student", "url": url_for("erp.create_student"), "icon": "bi-person-plus"},
            {"label": "New Department", "url": url_for("erp.create_department"), "icon": "bi-building"},
            {"label": "New Course", "url": url_for("erp.create_course"), "icon": "bi-book"},
            {"label": "New Exam", "url": url_for("erp.exams") + "#newExam" if url_for("erp.exams") else url_for("erp.exams"), "icon": "bi-card-checklist"},
        ],
    )


@erp_bp.route("/students")
def students():
    query = request.args.get("q", "").strip()
    students = student_service.get_all()

    if query:
        students = [
            student for student in students
            if query.lower() in (student.student_code or "").lower()
            or query.lower() in (student.first_name or "").lower()
            or query.lower() in (student.last_name or "").lower()
            or query.lower() in (student.email or "").lower()
        ]

    return render_template(
        "students/index.html",
        active_page="students",
        students=students,
        departments=department_service.get_all(),
        query=query,
    )


@erp_bp.route("/students/new", methods=["GET", "POST"])
def create_student():
    departments = department_service.get_all()
    if request.method == "POST":
        try:
            payload = student_schema.load(request.form)
            student = Student(**payload)
            student_service.create(student)
            flash("Student created successfully.", "success")
            return redirect(url_for("erp.students"))
        except ValidationError as error:
            flash("Failed to save student. " + str(error.messages), "danger")

    return render_template(
        "students/form.html",
        active_page="students",
        student=None,
        departments=departments,
        status_options=STATUS_OPTIONS,
        form_action=url_for("erp.create_student"),
        title="Add New Student",
    )


@erp_bp.route("/students/<int:student_id>/edit", methods=["GET", "POST"])
def edit_student(student_id):
    student = student_service.get_by_id(student_id)
    if not student:
        flash("Student record not found.", "warning")
        return redirect(url_for("erp.students"))

    if request.method == "POST":
        try:
            payload = student_schema.load(request.form)
            for field, value in payload.items():
                setattr(student, field, value)
            student_service.update(student)
            flash("Student updated successfully.", "success")
            return redirect(url_for("erp.students"))
        except ValidationError as error:
            flash("Failed to update student. " + str(error.messages), "danger")

    return render_template(
        "students/form.html",
        active_page="students",
        student=student,
        departments=department_service.get_all(),
        status_options=STATUS_OPTIONS,
        form_action=url_for("erp.edit_student", student_id=student.id),
        title="Edit Student",
    )


@erp_bp.route("/students/<int:student_id>/delete", methods=["POST"])
def delete_student(student_id):
    student = student_service.get_by_id(student_id)
    if not student:
        flash("Student record not found.", "warning")
    else:
        student_service.delete(student)
        flash("Student deleted successfully.", "success")
    return redirect(url_for("erp.students"))


@erp_bp.route("/departments")
def departments():
    try:
        query = request.args.get("q", "").strip()
        departments_list = safe_get_all(department_service.get_all)
        if query and departments_list:
            try:
                departments_list = [d for d in departments_list if query.lower() in (d.department_name or "").lower()]
            except:
                pass
        return render_template(
            "departments/index.html",
            active_page="departments",
            departments=departments_list,
            query=query,
        )
    except Exception as e:
        flash(f'Error loading departments: {str(e)[:100]}', 'danger')
        return render_template("departments/index.html", active_page="departments", departments=[], query="")


@erp_bp.route("/departments/new", methods=["GET", "POST"])
def create_department():
    try:
        if request.method == "POST":
            try:
                payload = department_schema.load(request.form)
                department_service.create(app.models.Department(**payload))
                flash("Department created successfully.", "success")
                return redirect(url_for("erp.departments"))
            except ValidationError as error:
                flash("Failed to create department. " + str(error.messages), "danger")

        return render_template(
            "departments/form.html",
            active_page="departments",
            department=None,
            status_options=["Active", "Inactive"],
            form_action=url_for("erp.create_department"),
            title="Add New Department",
        )
    except Exception as e:
        flash(f'Error: {str(e)[:100]}', 'danger')
        return redirect(url_for("erp.departments"))


@erp_bp.route("/departments/<int:department_id>/edit", methods=["GET", "POST"])
def edit_department(department_id):
    try:
        department = department_service.get_by_id(department_id)
        if not department:
            flash("Department not found.", "warning")
            return redirect(url_for("erp.departments"))

        if request.method == "POST":
            try:
                payload = department_schema.load(request.form)
                for field, value in payload.items():
                    setattr(department, field, value)
                department_service.update(department)
                flash("Department updated successfully.", "success")
                return redirect(url_for("erp.departments"))
            except ValidationError as error:
                flash("Failed to update department. " + str(error.messages), "danger")

        return render_template(
            "departments/form.html",
            active_page="departments",
            department=department,
            status_options=["Active", "Inactive"],
            form_action=url_for("erp.edit_department", department_id=department.id),
            title="Edit Department",
        )
    except Exception as e:
        flash(f'Error: {str(e)[:100]}', 'danger')
        return redirect(url_for("erp.departments"))


@erp_bp.route("/departments/<int:department_id>/delete", methods=["POST"])
def delete_department(department_id):
    try:
        department = department_service.get_by_id(department_id)
        if not department:
            flash("Department not found.", "warning")
        else:
            department_service.delete(department)
            flash("Department deleted successfully.", "success")
    except Exception as e:
        flash(f'Error deleting department: {str(e)[:100]}', 'danger')
    return redirect(url_for("erp.departments"))


@erp_bp.route("/faculty")
def faculty():
    query = request.args.get("q", "").strip()
    faculty_members = safe_get_all(faculty_service.get_all, error_msg="Could not load faculty")
    if query:
        try:
            faculty_members = faculty_service.search(query)
        except:
            pass
    return render_template(
        "faculty/index.html",
        active_page="faculty",
        faculty=faculty_members,
        departments=department_service.get_all(),
        query=query,
    )


@erp_bp.route("/faculty/new", methods=["GET", "POST"])
def create_faculty():
    if request.method == "POST":
        try:
            payload = faculty_schema.load(request.form)
            faculty_service.create(app.models.Faculty(**payload))
            flash("Faculty member created successfully.", "success")
            return redirect(url_for("erp.faculty"))
        except ValidationError as error:
            flash("Failed to create faculty member. " + str(error.messages), "danger")

    return render_template(
        "faculty/form.html",
        active_page="faculty",
        faculty=None,
        departments=department_service.get_all(),
        status_options=STATUS_OPTIONS,
        form_action=url_for("erp.create_faculty"),
        title="Add Faculty Member",
    )


@erp_bp.route("/faculty/<int:faculty_id>/edit", methods=["GET", "POST"])
def edit_faculty(faculty_id):
    faculty_member = faculty_service.get_by_id(faculty_id)
    if not faculty_member:
        flash("Faculty member not found.", "warning")
        return redirect(url_for("erp.faculty"))

    if request.method == "POST":
        try:
            payload = faculty_schema.load(request.form)
            for field, value in payload.items():
                setattr(faculty_member, field, value)
            faculty_service.update(faculty_member)
            flash("Faculty member updated successfully.", "success")
            return redirect(url_for("erp.faculty"))
        except ValidationError as error:
            flash("Failed to update faculty member. " + str(error.messages), "danger")

    return render_template(
        "faculty/form.html",
        active_page="faculty",
        faculty=faculty_member,
        departments=department_service.get_all(),
        status_options=STATUS_OPTIONS,
        form_action=url_for("erp.edit_faculty", faculty_id=faculty_member.id),
        title="Edit Faculty Member",
    )


@erp_bp.route("/faculty/<int:faculty_id>/delete", methods=["POST"])
def delete_faculty(faculty_id):
    faculty_member = faculty_service.get_by_id(faculty_id)
    if not faculty_member:
        flash("Faculty member not found.", "warning")
    else:
        faculty_service.delete(faculty_member)
        flash("Faculty member deleted successfully.", "success")
    return redirect(url_for("erp.faculty"))


@erp_bp.route("/courses")
def courses():
    query = request.args.get("q", "").strip()
    course_list = safe_get_all(course_service.get_all, error_msg="Could not load courses")
    if query:
        try:
            course_list = course_service.search(query)
        except:
            pass
    return render_template(
        "courses/index.html",
        active_page="courses",
        courses=course_list,
        departments=department_service.get_all(),
        query=query,
    )


@erp_bp.route("/courses/new", methods=["GET", "POST"])
def create_course():
    if request.method == "POST":
        try:
            payload = course_schema.load(request.form)
            course_service.create(app.models.Course(**payload))
            flash("Course created successfully.", "success")
            return redirect(url_for("erp.courses"))
        except ValidationError as error:
            flash("Failed to create course. " + str(error.messages), "danger")

    return render_template(
        "courses/form.html",
        active_page="courses",
        course=None,
        departments=department_service.get_all(),
        status_options=["Active", "Inactive"],
        form_action=url_for("erp.create_course"),
        title="Add New Course",
    )


@erp_bp.route("/courses/<int:course_id>/edit", methods=["GET", "POST"])
def edit_course(course_id):
    course = course_service.get_by_id(course_id)
    if not course:
        flash("Course not found.", "warning")
        return redirect(url_for("erp.courses"))

    if request.method == "POST":
        try:
            payload = course_schema.load(request.form)
            for field, value in payload.items():
                setattr(course, field, value)
            course_service.update(course)
            flash("Course updated successfully.", "success")
            return redirect(url_for("erp.courses"))
        except ValidationError as error:
            flash("Failed to update course. " + str(error.messages), "danger")

    return render_template(
        "courses/form.html",
        active_page="courses",
        course=course,
        departments=department_service.get_all(),
        status_options=["Active", "Inactive"],
        form_action=url_for("erp.edit_course", course_id=course.id),
        title="Edit Course",
    )


@erp_bp.route("/courses/<int:course_id>/delete", methods=["POST"])
def delete_course(course_id):
    course = course_service.get_by_id(course_id)
    if not course:
        flash("Course not found.", "warning")
    else:
        course_service.delete(course)
        flash("Course deleted successfully.", "success")
    return redirect(url_for("erp.courses"))


@erp_bp.route("/subjects")
def subjects():
    query = request.args.get("q", "").strip()
    subject_list = safe_get_all(subject_service.get_all, error_msg="Could not load subjects")
    if query:
        try:
            subject_list = subject_service.search(query)
        except:
            pass
    return render_template(
        "subjects/index.html",
        active_page="subjects",
        subjects=subject_list,
        courses=safe_get_all(course_service.get_all),
        faculty=safe_get_all(faculty_service.get_all),
        query=query,
    )


@erp_bp.route("/subjects/new", methods=["GET", "POST"])
def create_subject():
    if request.method == "POST":
        try:
            payload = subject_schema.load(request.form)
            subject_service.create(app.models.Subject(**payload))
            flash("Subject created successfully.", "success")
            return redirect(url_for("erp.subjects"))
        except ValidationError as error:
            flash("Failed to create subject. " + str(error.messages), "danger")

    return render_template(
        "subjects/form.html",
        active_page="subjects",
        subject=None,
        courses=course_service.get_all(),
        faculty=faculty_service.get_all(),
        status_options=["Active", "Inactive"],
        form_action=url_for("erp.create_subject"),
        title="Add New Subject",
    )


@erp_bp.route("/subjects/<int:subject_id>/edit", methods=["GET", "POST"])
def edit_subject(subject_id):
    subject = subject_service.get_by_id(subject_id)
    if not subject:
        flash("Subject not found.", "warning")
        return redirect(url_for("erp.subjects"))

    if request.method == "POST":
        try:
            payload = subject_schema.load(request.form)
            for field, value in payload.items():
                setattr(subject, field, value)
            subject_service.update(subject)
            flash("Subject updated successfully.", "success")
            return redirect(url_for("erp.subjects"))
        except ValidationError as error:
            flash("Failed to update subject. " + str(error.messages), "danger")

    return render_template(
        "subjects/form.html",
        active_page="subjects",
        subject=subject,
        courses=course_service.get_all(),
        faculty=faculty_service.get_all(),
        status_options=["Active", "Inactive"],
        form_action=url_for("erp.edit_subject", subject_id=subject.id),
        title="Edit Subject",
    )


@erp_bp.route("/subjects/<int:subject_id>/delete", methods=["POST"])
def delete_subject(subject_id):
    subject = subject_service.get_by_id(subject_id)
    if not subject:
        flash("Subject not found.", "warning")
    else:
        subject_service.delete(subject)
        flash("Subject deleted successfully.", "success")
    return redirect(url_for("erp.subjects"))


@erp_bp.route("/attendance")
def attendance():
    query = request.args.get("q", "").strip()
    attendance_records = safe_get_all(attendance_service.get_all, error_msg="Could not load attendance")
    if query:
        try:
            attendance_records = attendance_service.search(query)
        except:
            pass
    return render_template(
        "attendance/index.html",
        active_page="attendance",
        attendance=attendance_records,
        query=query,
    )


@erp_bp.route("/exams")
def exams():
    query = request.args.get("q", "").strip()
    exam_list = safe_get_all(exam_service.get_all, error_msg="Could not load exams")
    if query:
        try:
            exam_list = exam_service.search(query)
        except:
            pass
    return render_template(
        "exams/index.html",
        active_page="exams",
        exams=exam_list,
        query=query,
    )


@erp_bp.route("/fees")
def fees():
    query = request.args.get("q", "").strip()
    fees_list = safe_get_all(fee_service.get_all, error_msg="Could not load fees")
    if query:
        fees_list = [
            fee for fee in fees_list
            if query.lower() in (fee.academic_year or "").lower()
        ]
    return render_template(
        "fees/index.html",
        active_page="fees",
        fees=fees_list,
        query=query,
    )


@erp_bp.route("/payments")
def payments():
    query = request.args.get("q", "").strip()
    payments_list = safe_get_all(payment_service.get_all, error_msg="Could not load payments")
    if query:
        payments_list = [
            payment for payment in payments_list
            if query.lower() in (payment.payment_mode or "").lower()
            or query.lower() in (payment.transaction_reference or "").lower()
        ]
    return render_template(
        "payments/index.html",
        active_page="payments",
        payments=payments_list,
        query=query,
    )


@erp_bp.route("/users")
def users():
    query = request.args.get("q", "").strip()
    users_list = safe_get_all(user_service.get_all, error_msg="Could not load users")
    if query:
        users_list = [
            user for user in users_list
            if query.lower() in (user.username or "").lower()
            or query.lower() in (user.email or "").lower()
        ]
    return render_template(
        "users/index.html",
        active_page="users",
        users=users_list,
        query=query,
    )


@erp_bp.route("/roles")
def roles():
    return render_template(
        "roles/index.html",
        active_page="roles",
        roles=safe_get_all(role_service.get_all),
    )


@erp_bp.route("/notifications")
def notifications():
    return render_template(
        "notifications/index.html",
        active_page="notifications",
        notifications=notification_service.get_all(),
    )


@erp_bp.route("/audit-logs")
def audit_logs():
    return render_template(
        "audit_logs/index.html",
        active_page="audit_logs",
        audit_logs=audit_log_service.get_all(),
    )
