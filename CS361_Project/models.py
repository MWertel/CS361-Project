from django.db import models

class Account(models.Model):

    id = models.IntegerField(unique = True, primary_key= True)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length = 30)
    role = models.CharField(max_length=30)

class Supervisor(models.Model):
    id = models.OneToOneField("Account", primary_key= True, on_delete=models.CASCADE)
    name = models.CharField(max_length= 30)
    email = models.CharField(max_length= 30)
    telephone = models.CharField(max_length= 20)
    address = models.CharField(max_length = 40)

class Instructor(models.Model):

    id = models.OneToOneField("Account", primary_key= True, on_delete= models.CASCADE)
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    telephone = models.CharField(max_length=20)
    address = models.CharField(max_length=40)

class TA(models.Model):
    id = models.OneToOneField("Account", primary_key= True, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    telephone = models.CharField(max_length=20)
    address = models.CharField(max_length=40)
