from django.core import mail
from django.test import TestCase
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