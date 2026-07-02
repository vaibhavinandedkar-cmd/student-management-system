from flask import Blueprint, jsonify, request

from app.models.student import Student
from app.schemas.student_schema import (
    StudentCreateSchema,
    StudentResponseSchema
)
from app.services.student_service import StudentService

student_bp = Blueprint("students", __name__)

student_service = StudentService()

student_create_schema = StudentCreateSchema()
student_response_schema = StudentResponseSchema()
students_response_schema = StudentResponseSchema(many=True)


@student_bp.route("/", methods=["GET"])
def get_students():
    """
    Get all students
    """

    students = student_service.get_all_students()

    return jsonify(
        students_response_schema.dump(students)
    ), 200


@student_bp.route("/", methods=["POST"])
def create_student():
    """
    Create a new student
    """

    data = request.get_json()

    errors = student_create_schema.validate(data)

    if errors:
        return jsonify({
            "success": False,
            "errors": errors
        }), 400

    student = Student(
        student_code=data["student_code"],
        first_name=data["first_name"],
        last_name=data["last_name"],
        email=data["email"],
        phone=data.get("phone"),
        gender=data.get("gender"),
        department=data.get("department"),
        semester=data.get("semester"),
        address=data.get("address")
    )

    student = student_service.create_student(student)

    return jsonify({
        "success": True,
        "message": "Student created successfully.",
        "data": student_response_schema.dump(student)
    }), 201
