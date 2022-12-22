from django.test import TestCase, Client
from CS361_Project.models import Course, LabSection, Account, Course_LabSection


class test_Unassign(TestCase):
    client = None

    def setUp(self):
        course1 = Course(id=337, name="System Programming", department="CompSci")
        course1.save()
        labsection1 = LabSection(id=803, name="System Programming", department="CompSci")
        labsection1.save()
        account = Account(id=1, username="test", password="test", role="instructor", name="Jane Doe", email="janedoe@uwm.edu", telephone="222-222-2222", address="5678 Jane Street")
        account.save()
        course_lab = Course_LabSection(course=course1, labsection=labsection1)
        course_lab.save()
        self.client = Client()

    def test_NoUsername(self):
        response = self.client.post('/assign/removeUser/', {"user": None, "course": self.client.session.get("course"), "lab": self.client.session.get("lab")})
        message = response.context['error']
        self.assertEqual("There needs to be an user to remove Course and/or Lab Section assignment", message)

    def test_NoCourse(self):
        response = self.client.post('/assign/removeUser/', {"user": self.client.session.get("account"), "course": None, "lab": self.client.session.get("lab")})
        message = response.context['error']
        self.assertEqual("There needs to be a course or lab section to remove user from", message)

    def test_NoLabSection(self):
        response = self.client.post('/assign/removeUser/', {"user": self.client.session.get("account"), "course": self.client.session.get("course"), "lab": None})
        message = response.context['error']
        self.assertEqual("There needs to be a course or lab section to remove user from", message)
