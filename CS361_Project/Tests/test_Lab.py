from CS361_Project.models import Course
from django.test import Client, TestCase


class test_Lab(TestCase):
    client = None

    def setUp(self):
        course1 = Course(name="System Programming", id=337, department="CompSci")
        course1.save()
        self.client = Client()

    def test_CreateLabNoCourse(self):
        response = self.client.post('/course/createLab/', {"course": None})
        message = response.context['error']
        self.assertEqual("Lab Section needs to belong to a Course", message)

    def test_CreateLabNoName(self):
        response = self.client.post('/course/createLab/', {"course": 'System Programming', "name": '', "department": 'CompSci'})
        message = response.context['error']
        self.assertEqual("Name of the Lab Section cannot be empty", message)

    def test_CreateLabNoDepartment(self):
        response = self.client.post('/course/createLab/', {"course": 'System Programming', "name": '803', "department": ''})
        message = response.context['error']
        self.assertEqual("Lab Section needs a department", message)

    def test_EditLabNoneChosen(self):
        response = self.client.post('/course/editLab/', {"course": 'System Programming', "lab": None})
        message = response.context['error']
        self.assertEqual("A Lab Section must be chosen", message)

    def test_DeleteLabNoneChosen(self):
        response = self.client.post('/course/deleteLab/', {"course": 'System Programming', "lab": None})
        message = response.context['error']
        self.assertEqual("No Lab Section was selected", message)
