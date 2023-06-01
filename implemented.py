from dao.lecture_dao import LectureDAO
from dao.models.lecture import LectureSchema
from services.lecture_service import LectureService
from setup_db import db

lecture_dao = LectureDAO(db.session)
lecture_service = LectureService(dao=lecture_dao)

lecture_schema = LectureSchema()
lectures_schema = LectureSchema(many=True)
