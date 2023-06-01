from setup_db import db
from marshmallow import Schema, fields


class Lecture(db.Model):
    __tablename__ = 'lecture'

    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(20))
    lecture_date = db.Column(db.String(10))
    full_name = db.Column(db.String(30))
    class_number = db.Column(db.Integer)


class LectureSchema(Schema):
    id = fields.Int(dump_only=True)
    subject = fields.Str()
    lecture_date = fields.Str()
    full_name = fields.Str()
    class_number = fields.Int()
