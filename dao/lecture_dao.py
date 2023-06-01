from dao.models.lecture import Lecture


class LectureDAO:

    def __init__(self, session):
        self.session = session

    def get_one(self, lid):
        return self.session.query(Lecture).get(lid)

    def get_all(self):
        return self.session.query(Lecture).all()

    def create(self, data):
        lecture = Lecture(**data)

        self.session.add(lecture)
        self.session.commit()

        return lecture

    def update(self, lecture):
        self.session.add(lecture)
        self.session.commit()

    def delete(self, lid):
        lecture = self.get_one(lid)

        self.session.delete(lecture)
        self.session.commit()
