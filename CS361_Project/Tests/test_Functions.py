from django.test import TestCase, Client
from CS361_Project.functions import generateID, changeName,changePassword, changeRole,changeEmail,changeAddress,changePhoneNum
from django.test import TestCase, Client
from CS361_Project.models import Account, Supervisor


# Tests for Supervisor Creating Accounts


class TestFunctions(TestCase):

    def testIDGeneration(self):

        #the first ID created ever, must be one
        #new accounts is created
        username = "Steve"
        account = Account(id = generateID(username), username = username, password = "SteveMaximus", role = "Supervisor")
        account.save()

        self.assertEqual(hash(username),account.id)

    def setUp(self):
        self.account = Account(id=2, username="JohnD", password="12345", role="Supervisor", name="John",
                               email="john.deo@uwm.edu", telephone="(+1)111-222-3333", address="2 Street")
        self.account.save()

        self.account2 = Account(id=1, username="JoshB", password="12345", role="Instructor", name="Josh",
                               email="josh.bideo@uwm.edu", telephone="(+1)111-222-3333", address="2 Street")
        self.account2.save()

    def testNullName(self):
        with self.assertRaises(ValueError, msg="Null value fails raise ValueError"):
            changeName(self.account)

    def testInvalidName(self):

        with self.assertRaises(TypeError, msg="Name of Numbers fails to raise ValueError"):
            changeName(self.account,123)

    def testChangeEmail(self):
        changeEmail(self.account,"john.doe@uwm.edu")
        self.assertEqual("john.doe@uwm.edu", self.account.email)

    def testChangeRole(self):
        changeRole(self.account,"Instructor")
        self.assertEqual("Instructor", self.account.role)

    def testChangePhone(self):
        changePhoneNum(self.account,"5558675309")
        self.assertEqual("5558675309", self.account.telephone)

    def testChangeAddress(self):
        changeAddress(self.account,"1234 test ave.")
        self.assertEqual("1234 test ave.", self.account.address)

    def testChangePassword(self):
        changePassword(self.account,"New Password")
        self.assertEqual("New Password",self.account.password)

    def testInvalidPassword(self):
        with self.assertRaises(TypeError, msg="Name of Numbers fails to raise ValueError"):
            changePassword(self.account,v = [])