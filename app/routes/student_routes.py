from flask import Blueprint, jsonify

student_bp = Blueprint(
    "students",
    __name__
)


@student_bp.route(
    "/",
    methods=["GET"]
)
def get_students():
    """
    Get all students.
    """

    return jsonify(
        {
            "message": "Student API Working",
            "status": "success"
        }
    )
