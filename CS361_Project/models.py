from django.db import models


class Account(models.Model):
    id = models.IntegerField(unique = True, primary_key= True)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length = 30)
    role = models.CharField(max_length=30, null= True)
    name = models.CharField(max_length= 30, null= True)
    email = models.CharField(max_length= 30, null= True)
    telephone = models.CharField(max_length= 20, null= True)
    address = models.CharField(max_length = 40, null= True)

class Supervisor(models.Model):
    supervisorAccount = models.ForeignKey("Account", on_delete=models.CASCADE, default=None)

    def createCourse(self, department, courseNum, courseName):
        pass

    def deleteCourse(self, department, courseNum):
        pass

    def editCourse(self, department, courseNum):
        pass

class Instructor(models.Model):
    instructorAccount = models.ForeignKey("Account", on_delete = models.CASCADE, default=None)
    course = models.ForeignKey("Course", on_delete= models.SET_NULL, null= True)
    labSection = models.ForeignKey("LabSection",on_delete= models.SET_NULL, null= True)

class TA(models.Model):
    TAAccount = models.ForeignKey("Account", on_delete = models.CASCADE, default=None)
    course = models.ForeignKey("Course", on_delete= models.SET_NULL, null= True)
    labSection = models.ForeignKey("LabSection",on_delete= models.SET_NULL, null= True)

class LabSection(models.Model):
    id = models.IntegerField(primary_key = True)
    name = models.CharField(max_length = 50)
    departament = models.CharField(max_length = 30)


class Course(models.Model):
    id = models.IntegerField(primary_key = True)
    name = models.CharField(max_length = 50)
    departament = models.CharField(max_length=30)

#Not necessary, just use the models system to create and save on the Supervisor, look at the Database tests for ideas
##    def __init__(self, department, courseNum, name):
##       self.department = department
##        self.courseNum = courseNum
##        self.name = name

    def __str__(self):
        pass

    def setName(self, name):
        pass

    def getName(self):
        pass

    def setCourseNum(self, courseNum):
        pass

    def getCourseNum(self):
        pass

    def getDepartment(self):
        pass

    def setDepartment(self, department):
        pass


