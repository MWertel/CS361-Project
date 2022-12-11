from django.test import TestCase
from CS361_Project.models import Course


class test_Course(TestCase):

    def setUp(self):
        self.course = Course(name = "CompSci", id = 150, department="Survey of Computer Science")

    #Tests for setName
    def test_SetName(self):
        self.course.setName("System Programming")
        self.assertEqual("System Programming", self.course.name,
                         msg="Course name should be \"System Programming\" was \"" + self.course.name + "\"")

    def test_WrongArgType(self):
        with self.assertRaises(TypeError, msg="Course name should be a string"):
            self.course.setName(25)

    def test_TooManyArgs(self):
        with self.assertRaises(TypeError, msg="Too many arguments"):
            self.course.setName("System Programming", "Computer Architecture")

    def test_TooLittleArgs(self):
        with self.assertRaises(TypeError, msg="Not enough arguments"):
            self.course.setName()

    def test_GetCourseName(self):
        self.assertEqual("Survey of Computer Science", self.course.name,
                         msg="Course name should be \"Survey of Computer Science\" was \"" + self.course.name + "\"")

    #Tests for getCourseNum
    def test_GetCourseNum(self):
        self.assertTrue(self.course.getCourseNum() == 150,
                        msg="Course number should be \"150\" was \"" + self.course.getCourseNum() + "\"")

    #Tests for __init__
    def test_Department(self):
        self.assertEqual("CompSci", self.course.department,
                         msg="Department should be \"CompSci\" was \"" + self.course.department + "\"")

    def test_CourseNum(self):
        self.assertTrue(self.course.courseNum == 150,
                        msg="Course number should be \"150\" was \"" + self.course.courseNum + "\"")

    def test_CourseName(self):
        self.assertEqual("Survey of Computer Science", self.course.name,
                         msg="Course name should be \"Survey of Computer Science\" was \"" + self.course.name + "\"")

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

    def test_InitTooManyArgs(self):
        with self.assertRaises(TypeError, msg="Too many arguments"):
            a = Course("CompSci", 150, "Survey of Computer Science", "Soronson", 1300)

    def test_InitTooLittleArgs(self):
        with self.assertRaises(TypeError, msg="Too little arguments"):
            a = Course("CompSci", 150, "Survey of Computer Science")

    def test_InitNoParameters(self):
        with self.assertRaises(TypeError, msg="There are no parameters"):
            a = Course()

    #Tests for setCourseNum
    def test_SetCourseNum(self):
        self.course.setCourseNum(250)
        self.assertTrue(self.course.courseNum == 250,
                        msg="Course number should be \"250\" was \"" + self.course.courseNum + "\"")

    def test_SetNumWrongArgs(self):
        with self.assertRaises(TypeError, msg="Course number should be an integer"):
            self.course.setCourseNum("150")

    def test_NegativeCourseNumber(self):
        with self.assertRaises(TypeError, msg="Course number should be a positive number"):
            self.course.setCourseNum(-150)

    def test_SetNumTooManyArgs(self):
        with self.assertRaises(TypeError, msg="Too many arguments"):
            self.course.setCourseNum(250, 251)

    def test_SetNumTooLittleArgs(self):
        with self.assertRaises(TypeError, msg="Not enough arguments"):
            self.course.setCourseNum()

    #Tests for setDepartment
    def test_SetDepartment(self):
        self.course.setDepartment("Math")
        self.assertEqual("Math", self.course.department,
                         msg="Department should be \"Math\" was \"" + self.course.department + "\"")

    def test_setDepartmentWrongArgs(self):
        with self.assertRaises(TypeError, msg="Department should be a string"):
            self.course.setDepartment(150)

    def test_setDepartmentTooManyArgs(self):
        with self.assertRaises(TypeError, msg="Too many arguments"):
            self.course.setDepartment("Math", "Art")

    def test_setDepartmentTooLittleArgs(self):
        with self.assertRaises(TypeError, msg="Not enough arguments"):
            self.course.setDepartment()

    #Tests for __str__
    def test_Display(self):
        self.assertEqual("CompSci 150: Survey of Computer Science", self.course.__str__(),
                         msg="String should be \"CompSci 150: Survey of Computer Science\" was \""
                         + self.course.__str__() + "\"")

    #Tests for getDepartment
    def test_GetDepartment(self):
        self.assertEqual("CompSci", self.course.getDepartment,
                         msg="Department should be \"CompSci\" was \"" + self.course.getDepartment() + "\"")
