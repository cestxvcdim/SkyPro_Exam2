from dao.lecture_dao import LectureDAO


class LectureService:
    """
    This class is 2nd layer, which works with business-logic of the application.

    Methods of the class handle a data
    And give this to next layer.
    """
    def __init__(self, dao: LectureDAO):
        """Defines DAO for working with database's session."""

        self.dao = dao

    def get_one(self, lid):
        """Returns object by id."""

        return self.dao.get_one(lid)

    def get_all(self):
        """Returns all objects"""

        return self.dao.get_all()

    def create(self, data):
        """Create new object of model."""

        return self.dao.create(data)

    def update(self, data, lid):
        """Update object fully."""

        lecture = self.dao.get_one(lid)

        lecture.subject = data.get("subject")
        lecture.lecture_date = data.get("lecture_date")
        lecture.full_name = data.get("full_name")
        lecture.class_number = data.get("class_number")

        self.dao.update(lecture)

    def update_partial(self, data, lid):
        """Update object partially."""

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
        """Delete object."""

        self.dao.delete(lid)
