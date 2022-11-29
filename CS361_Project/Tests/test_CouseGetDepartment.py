from django.test import TestCase
from CS361_Project.models import Course


class test_GetDepartment(TestCase):

    def setUp(self):
        self.rightArgs = Course("CompSci", 150, "Survey of Computer Science", "Soronson")

    def test_GetDepartment(self):
        self.setUp()
        self.assertEqual("CompSci", self.rightArgs.getDepartment, msg="Department should be CompSci was "
                                                                      + self.rightArgs.getDepartment())
