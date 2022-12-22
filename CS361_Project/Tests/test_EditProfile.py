from django.test import Client, TestCase
from CS361_Project.models import Account


class test_EditProfile(TestCase):
    client = None
    passwordError = "New Password must have at least one digit, one upper case character, one lower case character, one special symbol, and at least 5 characters"

    def setUp(self):
        account = Account(id=1, username="test", password="test", role="Supervisor", name="John Doe", email="johndoe@uwm.edu", telephone="111-111-1111", address="1234 Test Street")
        account.save()

        self.client = Client()

    def test_PasswordNoSpecialChar(self):
        response = self.client.post('/profile/edit/', {"NewPassword": 'HelloWorld123', "NewPasswordRepeat": 'HelloWorld123'})
        message = response.context['error']
        self.assertEqual(self.passwordError, message)

    def test_PasswordNoUpperCase(self):
        response = self.client.post('/profile/edit/', {"NewPassword": 'helloworld1234!', "NewPasswordRepeat": 'helloworld1234!'})
        message = response.context['error']
        self.assertEqual(self.passwordError, message)

    def test_PasswordNoLowerCase(self):
        response = self.client.post('/profile/edit/', {"NewPassword": 'HELLOWORLD1234!', "NewPasswordRepeat": 'HELLOWORLD1234!'})
        message = response.context['error']
        self.assertEqual(self.passwordError, message)

    def test_PasswordNoNumber(self):
        response = self.client.post('/profile/edit/', {"NewPassword": 'HelloWorld!', "NewPasswordRepeat": 'HelloWorld!'})
        message = response.context['error']
        self.assertEqual(self.passwordError, message)

    def test_PasswordsDontMatch(self):
        response = self.client.post('/profile/edit/', {"NewPassword": 'HelloWorld1234!', "NewPasswordRepeat": 'Helloworld1234!'})
        message = response.context['error']
        self.assertEqual("Passwords don't match", message)

    def test_WrongCurrentPassword(self):
        response = self.client.post('/profile/edit/', {"CurrentPassword": 'admin'})
        message = response.context['error']
        self.assertEqual("Current Password doesn't match with the user's", message)
