from django.test import TestCase, Client
from django.contrib.auth.models import User
from CS361_Project.models import Account, Supervisor, Instructor, TA


class DefaultLoginTests(TestCase):
    client = None

    def setUp(self):
        account = Account(id=1, username="Dan", password="123456", role="Supervisor", name="Dan Le",
                          email="danhcle@uwm.edu", telephone="111-111-111",
                          address="123 Street")
        account.save()
        self.client = Client()

    # Normal client's Post request.
    def testDoesNotExist(self):
        response = self.client.post('/', {'username': 'hey', 'password': '123456'})
        message = response.context['error']
        self.assertEqual('User does not exist', message)

    def testIncorrectPasswordMessage(self):
        response = self.client.post('/', {'username': 'Dan', 'password': "12345"})
        message = response.context['error']
        self.assertEqual("Incorrect Password", message)

    def testSuccessfulLogin(self):
        # Post the username + password
        response = self.client.post('/', {'username': 'Dan', 'password': '123456'})
        # Redirection to home only if user is logged-in
        self.assertRedirects(response, '/home/')

        # When login is successful, we can check for role
        userRole = self.client.session['role']
        self.assertEqual("Supervisor", userRole)

        # As well as checking the name of the logged-in user
        userName = self.client.session['name']
        self.assertEqual("Dan Le", userName)

        # Check if they are authenticated
        is_authenticated = self.client.session['is_authenticate']
        self.assertTrue(is_authenticated)

