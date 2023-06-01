from flask import request
from flask_restx import Resource, Namespace
from implemented import lecture_service, lecture_schema, lectures_schema


lecture_ns = Namespace('lectures')


@lecture_ns.route('/')
class LecturesView(Resource):

    def get(self):
        lectures = lecture_service.get_all()
        return lectures_schema.dump(lectures), 200

    def post(self):
        data = request.json
        new_lecture = lecture_service.create(data)

        return lecture_schema.dump(new_lecture), 201


@lecture_ns.route('/<int:lid>')
class LectureView(Resource):

    def get(self, lid):
        lecture = lecture_service.get_one(lid)
        return lecture_schema.dump(lecture), 200

    def put(self, lid):
        data = request.json
        lecture_service.update(data, lid)

        lecture = lecture_service.get_one(lid)

        return lecture_schema.dump(lecture), 202

    def patch(self, lid):
        data = request.json
        lecture_service.update_partial(data, lid)

        lecture = lecture_service.get_one(lid)

        return lecture_schema.dump(lecture), 202

    def delete(self, lid):
        lecture_service.delete(lid)
        response = {"message": "Lecture has deleted successfully"}

        return response, 200
