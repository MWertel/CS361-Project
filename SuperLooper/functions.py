from django.core import mail
from django.test import TestCase
from CS361_Project.models import Course,LabSection,Course_LabSection, Account, TA, Instructor
import re


#This functions generates an ID based on a hash of the User's first username
def generateID(username):
    #We assing the ID based on a hash that uses the Users name
    return hash(username)

def changeName(account,change = "Null"):
    if type(change) != str:
        raise TypeError("Name of Numbers fails to raise ValueError")


    if change == "Null":
        raise ValueError("Null value fails raise ValueError")

    account.name = change
    account.save()

def changeEmail(account, change = "Null"):
    if type(change) != str:
        raise TypeError("Name of Numbers fails to raise ValueError")

    if change == "Null":
        raise ValueError("Null value fails raise ValueError")

    account.email = change
    account.save()

def changeRole(account, change = "Null"):
    if type(change) != str:
        raise TypeError("Name of Numbers fails to raise ValueError")

    if change == "Null":
        raise ValueError("Null value fails raise ValueError")

    account.role = change
    account.save()

def changeTelephone(account, change = "Null"):
    if type(change) != str:
        raise TypeError("Name of Numbers fails to raise ValueError")

    if change == "Null":
        raise ValueError("Null value fails raise ValueError")

    account.telephone = change
    account.save()

def changeAddress(account, other = "Null"):
    if type(other) != str:
        raise TypeError("Name of Numbers fails to raise ValueError")

    if other == "Null":
        raise ValueError("Null value fails raise ValueError")

    account.address = other
    account.save()

def changePassword(account,other = "Null"):

    if type(other) != str:
        raise TypeError("Name of Numbers fails to raise ValueError")

    if other == "Null":
        raise ValueError("Null value fails raise ValueError")

    account.password = other
    account.save()


def passwordChecker(password):
    #Checks the password to see if matches with the requirements
    #Returns true if so, false if not
    #one digit
    #one upper case
    #one lower case
    #at least 5 characters
    #one special character
    pattern = "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$"
    result = re.match(pattern,password)

    if result != None:
        return True
    else:
        return False


def sendEmail(message, sender, recipient):
    subject = "Notification!"
    return mail.send_mail(subject, message,
                          sender, recipient,
                          fail_silently=False)

def assignToTable(user,course, lab):
    if user.role == "Instructor":

        if len(list(Instructor.objects.filter(Account = user, course = course, labSection= lab))):
            return False#Wasn't able to assign due to assignment already being present

        newAssign = Instructor(Account = user, course = course, labSection = lab)
        newAssign.save()
        return True

    elif user.role == "TA":
        if len(list(TA.objects.filter(Account=user, course=course, labSection=lab))):
            return False  # Wasn't able to assign due to assignment already being present

        newAssign = TA(Account = user, course = course, labSection= lab)
        newAssign.save()
        return True

    return False#Didn't add anything


    #todo make some more tests for this one


def removeFromTable(user,course,lab):

    if user.role == "Instructor":
        toDelete = Instructor.objects.get(Account = user, course = course, labSection=lab)
        toDelete.delete()

    elif user.role == "TA":
        toDelete = TA.objects.get(Account=user, course=course, labSection=lab)
        toDelete.delete()
