from django.test import TestCase
from CS361_Project.models import Course


class test_TestInit(TestCase):

    def setUp(self):
        self.rightArgs = Course("CompSci", 150, "Survey of Computer Science", "Soronson")

    def test_Department(self):
        self.setUp()
        self.assertEqual("CompSci", self.rightArgs.department, msg="Department should be CompSci was "
                                                                   + self.rightArgs.department)

    def test_CourseNum(self):
        self.setUp()
        self.assertTrue(self.rightArgs.courseNum == 150, msg="Course number should be 150 was "
                                                             + self.rightArgs.courseNum)

    def test_CourseName(self):
        self.setUp()
        self.assertEqual("Survey of Computer Science", self.rightArgs.name, msg="Course name should be Survey of "
                                                                                "Computer Science was "
                                                                                + self.rightArgs.name)

    def test_Instructor(self):
        self.setUp()
        self.assertEqual("Soronson", self.rightArgs.instructor, msg="Instructor should be Soronson was "
                                                                    + self.rightArgs.instructor)

    def test_WrongDepartmentArg(self):
        with self.assertRaises(TypeError, msg="Department name should be a string"):
            a = Course(27, 150, "Survey of Computer Science", "Soronson")

    def test_WrongCourseNumArg(self):
        with self.assertRaises(TypeError, msg="Course Number should be an integer"):
            b = Course("CompSci", "150", "Survey of Computer Science", "Soronson")

    def test_NegativeCourseNum(self):
        with self.assertRaises(TypeError, msg="Course Number should be positive"):
            c = Course("CompSci", -150, "Survey of Cpmuter Science", "Soronson")

    def test_WrongCourseNameArg(self):
        with self.assertRaises(TypeError, msg="Course name should be a string"):
            d = Course("CompSci", 150, 45, "Soronson")

    def test_WrongInstructorArg(self):
        with self.assertRaises(TypeError, msg="Instructor should be a string"):
            e = Course("CompSci", 150, "Survey of Computer Science", 35)

    def test_TooManyArgs(self):
        with self.assertRaises(TypeError, msg="Too many arguments"):
            a = Course("CompSci", 150, "Survey of Computer Science", "Soronson", 1300)

    def test_TooLittleArgs(self):
        with self.assertRaises(TypeError, msg="Too little arguments"):
            a = Course("CompSci", 150, "Survey of Computer Science")
