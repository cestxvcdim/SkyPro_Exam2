from dao.models.lecture import Lecture


class LectureDAO:
    """
    This class is 3rd layer, which works with a database only.

    Methods of the class address to the database
    And get data from there
    Or put data there.
    """
    def __init__(self, session):
        """Defines a database's session."""

        self.session = session

    def get_one(self, lid):
        """Returns object by id from the database."""

        return self.session.query(Lecture).get(lid)

    def get_all(self):
        """Returns all objects from the database."""

        return self.session.query(Lecture).all()

    def create(self, data):
        """
        Create new object of model
        And put him to the database.

        Returns created object.
        """

        lecture = Lecture(**data)

        self.session.add(lecture)
        self.session.commit()

        return lecture

    def update(self, lecture):
        """
        Put transferred object to the database
        And update him by this way.

        Nothing returns.
        """

        self.session.add(lecture)
        self.session.commit()

    def delete(self, lid):
        """
        Get object by id from the database
        And delete him from there.

        Nothing returns.
        """

        lecture = self.get_one(lid)

        self.session.delete(lecture)
        self.session.commit()
