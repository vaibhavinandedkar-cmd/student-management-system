from marshmallow import Schema, fields, validate


class StudentSchema(Schema):
    """
    Student Request/Response Schema
    """

    id = fields.Integer(
        dump_only=True
    )

    student_code = fields.String(
        required=True,
        validate=validate.Length(
            min=3,
            max=20
        )
    )

    first_name = fields.String(
        required=True,
        validate=validate.Length(
            min=2,
            max=100
        )
    )

    last_name = fields.String(
        required=True,
        validate=validate.Length(
            min=2,
            max=100
        )
    )

    email = fields.Email(
        required=True
    )

    phone = fields.String()

    gender = fields.String()

    department = fields.String()

    semester = fields.Integer(
        validate=validate.Range(
            min=1,
            max=8
        )
    )

    address = fields.String()

    status = fields.String(
        dump_only=True
    )

    created_at = fields.DateTime(
        dump_only=True
    )

    updated_at = fields.DateTime(
        dump_only=True
    )
