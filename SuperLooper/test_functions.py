import SuperLooper
from SuperLooper import functions
from django.test import TestCase


class TestFunctions(TestCase):

    def test_generateID(self):
        thislist = []

        for x in range(10):
            thislist.append(functions.generateID())

        for x in thislist:
            if x < 0:
                self.assertRaises(ValueError, msg="Negative ID")

    def test_changeNameNumber(self):
        with self.assertRaises(TypeError, msg="Name Not a String"):
            SuperLooper.functions.changeName(4)

    def test_changeNameNull(self):
        with self.assertRaises(ValueError, msg="Null Name Change"):
            SuperLooper.functions.changeName("")

    def test_changeEmailNumber(self):
        with self.assertRaises(TypeError, msg="Email Not a String"):
            SuperLooper.functions.changeEmail(4)

    def test_changeEmailNull(self):
        with self.assertRaises(ValueError, msg="Null Email Change"):
            SuperLooper.functions.changeEmail("")

    def test_changeRoleNumber(self):
        with self.assertRaises(TypeError, msg="Role Not a String"):
            SuperLooper.functions.changeRole(4)

    def test_changeRoleNull(self):
        with self.assertRaises(ValueError, msg="Null Role Change"):
            SuperLooper.functions.changeRole("")

    def test_changeTelephoneNumber(self):
        with self.assertRaises(TypeError, msg="Telephone Not a String"):
            SuperLooper.functions.changeRole(4)

    def test_changeTelephoneNull(self):
        with self.assertRaises(ValueError, msg="Null Telephone Change"):
            SuperLooper.functions.changeRole("")

    def test_changeAddressNumber(self):
        with self.assertRaises(TypeError, msg="Address Not a String"):
            SuperLooper.functions.changeRole(4)

    def test_changeAddressNull(self):
        with self.assertRaises(ValueError, msg="Null Address Change"):
            SuperLooper.functions.changeRole("")
