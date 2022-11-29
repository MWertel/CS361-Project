from django.db import models

class Account(models.Model):

    id = models.IntegerField(unique = True, primary_key= True)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length = 30)
    role = models.CharField(max_length=30)

class Supervisor(models.Model):
    id = models.ForeignKey("Account", primary_key=True, on_delete= models.CASCADE)
    name = models.CharField(max_length= 30)
    email = models.CharField(max_length= 30)
    telephone = models.CharField(max_length= 20)
    address = models.CharField(max_length = 40)

    def createCourse(self, department, courseNum, courseName, instructor):
        pass

    def deleteCourse(self, department, courseNum):
        pass

    def editCourse(self, department, courseNum):
        pass


class Course(object):

    def __init__(self, department, courseNum, name, instructor):
        self.department = department
        self.courseNum = courseNum
        self.name = name
        self.instructor = instructor

    def setName(self, name):
        pass

    def getName(self):
        pass

    def setInstructor(self, instructor):
        pass

    def getInstructor(self):
        pass

    def setCourseNum(self, courseNum):
        pass

    def getCourseNum(self):
        pass

    def getDepartment(self):
        pass

    def setDepartment(self, department):
        pass



