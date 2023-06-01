import pytest
from unittest.mock import MagicMock
from dao.models.lecture import Lecture
from dao.lecture_dao import LectureDAO
from services.lecture_service import LectureService


@pytest.fixture
def test_lecture_dao():
    test_dao = LectureDAO(None)

    literature = Lecture(
        id=1,
        subject="Literature",
        lecture_date="13.09.2023",
        full_name="Tatyana Vladimirovna",
        class_number=101
    )
    english = Lecture(
        id=2,
        subject="English",
        lecture_date="15.09.2023",
        full_name="George Soloviev",
        class_number=312
    )
    mathematics = Lecture(
        id=3,
        subject="Mathematics",
        lecture_date="12.09.2023",
        full_name="Nataly Petrovna",
        class_number=404
    )

    test_dao.get_one = MagicMock(return_value=english)
    test_dao.get_all = MagicMock(return_value=[literature, english, mathematics])
    test_dao.create = MagicMock(return_value=Lecture(id=3))
    test_dao.update = MagicMock(return_value=None)
    test_dao.delete = MagicMock(return_value=None)

    return test_dao


class TestLectureService:

    @pytest.fixture(autouse=True)
    def test_lecture_service(self, test_lecture_dao):
        self.tls = LectureService(dao=test_lecture_dao)

    def test_get_one(self):
        lecture = self.tls.get_one(1)

        assert isinstance(lecture, Lecture)

    def test_get_all(self):
        lectures = self.tls.get_all()

        assert len(lectures) > 0
        assert isinstance(lectures[0], Lecture)

    def test_create(self):
        data = {
            "subject": "Coding",
            "lecture_date": "20.08.2023",
            "full_name": "Ivan Fufaev",
            "class_number": 200
        }
        lecture = self.tls.create(data)

        assert isinstance(lecture, Lecture)

    def test_update(self):
        data = {
            "subject": "Coding",
            "lecture_date": "20.08.2023",
            "full_name": "Ivan Fufaev",
            "class_number": 200
        }
        self.tls.update(data, 1)
        lecture = self.tls.get_one(1)

        assert isinstance(lecture, Lecture)
        assert lecture.text == "La la la"

    def test_update_partial(self):
        data = {
            "subject": "Coding",
            "lecture_date": "20.08.2023",
            "full_name": "Ivan Fufaev",
            "class_number": 200
        }
        self.tls.update(data, 2)
        lecture = self.tls.get_one(2)

        assert isinstance(lecture, Lecture)
        assert lecture.text == "La la la"

    def test_delete(self):
        lecture = self.tls.delete(1)

        assert lecture is None
