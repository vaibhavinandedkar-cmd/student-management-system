from marshmallow import Schema, fields, validate


class StudentCreateSchema(Schema):
    student_code = fields.String(required=True, validate=validate.Length(min=3, max=20))
    first_name = fields.String(required=True)
    last_name = fields.String(required=True)
    email = fields.Email(required=True)
    phone = fields.String()
    gender = fields.String()
    department = fields.String()
    semester = fields.Integer(validate=validate.Range(min=1, max=8))
    address = fields.String()


class StudentUpdateSchema(Schema):
    first_name = fields.String()
    last_name = fields.String()
    email = fields.Email()
    phone = fields.String()
    gender = fields.String()
    department = fields.String()
    semester = fields.Integer(validate=validate.Range(min=1, max=8))
    address = fields.String()
    status = fields.String()


class StudentResponseSchema(Schema):
    id = fields.Integer()
    student_code = fields.String()
    first_name = fields.String()
    last_name = fields.String()
    email = fields.Email()
    phone = fields.String()
    gender = fields.String()
    department = fields.String()
    semester = fields.Integer()
    address = fields.String()
    status = fields.String()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
