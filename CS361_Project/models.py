from django.db import models


class Account(models.Model):
    id = models.IntegerField(unique = True, primary_key= True)
    username = models.CharField(max_length=30, unique = True)
    password = models.CharField(max_length = 30)
    role = models.CharField(max_length=30, null=True) #username, password and role should not be null
    name = models.CharField(max_length= 30, null= True)
    email = models.CharField(max_length= 30, null= True)
    telephone = models.CharField(max_length= 20, null= True)
    address = models.CharField(max_length = 40, null= True)

class Supervisor(models.Model):
    supervisorAccount = models.ForeignKey("Account", on_delete=models.CASCADE, default=None)

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
    department = models.CharField(max_length = 30)


class Course(models.Model):
    id = models.IntegerField(primary_key = True)
    name = models.CharField(max_length = 50)
    department = models.CharField(max_length=30)

#Link Table
class Course_LabSection(models.Model):
    course = models.ForeignKey("Course",on_delete=models.CASCADE)
    labSection = models.ForeignKey("LabSection", on_delete=models.CASCADE)