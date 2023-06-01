from dao.lecture_dao import LectureDAO


class LectureService:

    def __init__(self, dao: LectureDAO):
        self.dao = dao

    def get_one(self, lid):
        return self.dao.get_one(lid)

    def get_all(self):
        return self.dao.get_all()

    def create(self, data):
        return self.dao.create(data)

    def update(self, data, lid):
        lecture = self.dao.get_one(lid)

        lecture.subject = data.get("subject")
        lecture.lecture_date = data.get("lecture_date")
        lecture.full_name = data.get("full_name")
        lecture.class_number = data.get("class_number")

        self.dao.update(lecture)

    def update_partial(self, data, lid):
        lecture = self.get_one(lid)

        if "subject" in data:
            lecture.subject = data.get("subject")
        if "lecture_date" in data:
            lecture.lecture_date = data.get("lecture_date")
        if "full_name" in data:
            lecture.full_name = data.get("full_name")
        if "class_number" in data:
            lecture.class_number = data.get("class_number")

        self.dao.update(lecture)

    def delete(self, lid):
        self.dao.delete(lid)
