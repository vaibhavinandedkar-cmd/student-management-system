from flask import Blueprint, jsonify

from app.services.student_service import StudentService

student_bp = Blueprint("students", __name__)

student_service = StudentService()


@student_bp.route("/", methods=["GET"])
def get_students():
    """
    Get all students
    """

    students = student_service.get_all_students()

    result = []

    for student in students:
        result.append({
            "id": student.id,
            "student_code": student.student_code,
            "first_name": student.first_name,
            "last_name": student.last_name,
            "email": student.email,
            "department": student.department,
            "semester": student.semester,
            "status": student.status
        })

    return jsonify(result), 200
