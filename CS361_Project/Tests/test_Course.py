from django.test import TestCase
from CS361_Project.models import Course
from django.test import Client


class test_Course(TestCase):
    client = None

    def setUp(self):
        course1 = Course(name = "Survey of Computer Science", id = 150, department = "CompSci")
        course1.save()
        course2 = Course(name = "Computer Architecture", id = 458, department = "CompSci")
        course2.save()
        self.client = Client()

    def test_CreateCourseNoName(self):
        response = self.client.post('/course/createCourse/', {"name": '', "id": 458, "department": 'CompSci'})
        message = response.context['error']
        self.assertEqual('Name of the Course cannot be empty', message)

    def test_CreateCourseNoDepartment(self):
        response = self.client.post('/course/createCourse/', {"name": 'Computer Architecture', "id": 458, "department": ''})
        message = response.context['error']
        self.assertEqual('Course needs a departament', message)

    def test_DeleteCourseNoneChosen(self):
        response = self.client.post('/course/deleteCourse', {"course": None})
        message = response.context['error']
        self.assertEqual('No Course was selected', message)

    def test_EditCourseNoneChosen(self):
        response = self.client.post('/course/editCourse', {"course": None})
        message = response.context['error']
        self.assertEqual("A Course must be chosen", message)

