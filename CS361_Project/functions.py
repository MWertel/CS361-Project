from .models import Account, Supervisor, Instructor, TA
import random as rand


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

def changePhoneNum(account, change = "Null"):
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