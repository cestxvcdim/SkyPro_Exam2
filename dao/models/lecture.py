from setup_db import db
from marshmallow import Schema, fields


class Lecture(db.Model):
    """
    Model of lecture.

    Example data:
    Lecture(
        id=1,
        subject="English",
        lecture_date="12.12.2023",
        full_name="Ivan Ivanov",
        class_number=200
    )
    """

    __tablename__ = 'lecture'

    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(20))
    lecture_date = db.Column(db.String(10))
    full_name = db.Column(db.String(30))
    class_number = db.Column(db.Integer)


class LectureSchema(Schema):
    """
    Schema of lecture's model.
    """

    id = fields.Int(dump_only=True)
    subject = fields.Str()
    lecture_date = fields.Str()
    full_name = fields.Str()
    class_number = fields.Int()
