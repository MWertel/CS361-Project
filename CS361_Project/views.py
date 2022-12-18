from django.middleware.csrf import rotate_token
from django.shortcuts import render, redirect
from django.views import View
from .models import Account, Supervisor, Instructor, TA, Course, LabSection
from .functions import generateID, changeName, changePassword, changeEmail, changeAddress,changeTelephone, passwordChecker


# Create your views here.

class Login(View):
    def get(self, request):
        if request.session.get('is_authenticate'):
            return redirect('home/')
        return render(request, "login.html", {"inputCSS": "validInputBox"})

    def post(self, request):
        Username = request.POST.get('username')
        Password = request.POST.get('password')
        if Password == '' or Username == '':
            return render(request, "login.html",
                          {"error": "Username or Password is missing", "inputCSS": "invalidInputBox",
                           "errorCSS": "failedError"})

        try:
            user = Account.objects.get(username=Username)
        except:
            return render(request, "login.html",
                          {"error": "User does not exist", "inputCSS": "invalidInputBox", "errorCSS": "failedError"})

        if user.password == Password:
            session = request.session
            session['is_authenticate'] = True
            session['role'] = user.role
            session['name'] = user.name
            return redirect('home/')
        else:
            return render(request, "login.html",
                          {"error": "Incorrect Password", "inputCSS": "invalidInputBox", "errorCSS": "failedError"})


class Home(View):
    def get(self, request):

        accounts = list(Account.objects.all())

        if request.session.get('is_authenticate'):
            return render(request, "Home.html", {"accounts": accounts})
        else:
            return render(request, "login.html")


#     No Post yet.


class ManageAccounts(View):
    def get(self, request):
        request.session['action'] = None
        return render(request, 'Accounts/Manage.html', {"validForm": 'invalid'})

    def post(self, request):
        request.session['action'] = None
        if request.POST.get('create') is not None:
            request.session['action'] = 'create'
        elif request.POST.get('edit') is not None:
            request.session['action'] = 'edit'
        else:
            request.session['action'] = 'delete'

        return render(request, 'Accounts/Manage.html')


class CreateAccount(View):

    def get(self, request):
        return render(request, 'Accounts/Manage.html', {"validForm": "valid"})

    def post(self, request):
        action = request.session["action"]

        if action == "create":
            username = request.POST.get("Username")
            if  len(list(Account.objects.filter(username = username))) > 0 :#username already exists
                error = "Username already exists in Database"
                return render(request, 'Accounts/Manage.html',{"error":error})

            role = request.POST.get("role")
            if role == None:#No role given, the user requires a role
                error = "Every user needs to have a role"
                return render(request, "Accounts/Manage.html", {"error":error})

            password = request.POST.get("Password")
            if passwordChecker(password) == False: #Bad Password
                error = "Password must have at least one digit, one upper case character, one lower case character, one special symbol, and at least 5 characters"
                return render(request,"Accounts/Manage.html", {"error":error})

            id = generateID(username)
            newAccount = Account(id = id, username = username,
                                 password = password,
                                 name = request.POST.get("Name"),
                                 role = role,
                                 email = request.POST.get("Email"),
                                 telephone = request.POST.get("Telephone"),
                                 address = request.POST.get("Address")
            )
            newAccount.save()

        return render(request, 'Accounts/Manage.html')


class EditAccount(View):

    def get(self, request):
        return render(request, 'Accounts/Manage.html')

    def post(self, request):
        action = request.session["action"]

        if action == "edit":
            username = request.POST.get("Username")
            if len(list(Account.objects.filter(username = username))) == 0 :  # username doesn't exists
                error = "Username not in Database"
                return render(request, 'Accounts/Manage.html',{"error":error})

            editAccount = Account.objects.get(username=username)
            if request.POST.get("Password") != "":
                if passwordChecker(request.POST.get("Password")) == False:  # Bad Password
                    error = "Password must have at least one digit, one upper case character, one lower case character, one special symbol, and at least 5 characters"
                    return render(request, "Accounts/Manage.html", {"error": error})
                changePassword(editAccount, request.POST.get("Password"))

            if request.POST.get("Name") != "":
                changeName(editAccount, request.POST.get("Name"))

            if request.POST.get("Email") != "":
                changeEmail(editAccount, request.POST.get("Email"))

            if request.POST.get("Telephone") != "":
                changeTelephone(editAccount, request.POST.get("Telephone"))

            if request.POST.get("Address") != "":
                changeAddress(editAccount, request.POST.get("Address"))

            editAccount.save()
        return render(request, 'Accounts/Manage.html')


class DeleteAccount(View):

    def get(self, request):
        return render(request, 'Accounts/Manage.html')

    def post(self, request):
        action = request.session["action"]

        if action == "delete":  #delete
            username = request.POST.get("username")
            if len(list(Account.objects.filter(username = username))) == 0 :  # username doesn't exists
                error = "Username not in Database"
                return render(request, 'Accounts/Manage.html',{"error":error})
            else:
                deleteAccount = Account.objects.get(username=username)
                deleteAccount.delete()
        return render(request, 'Accounts/Manage.html')


class Notification(View):
    def get(self, request):
        return render(request, 'NotificationForm.html')

    def post(self, request):
        recipients = request.POST.get('recipients')
        message = request.POST.get('message')
        return render(request, 'NotificationForm.html')


class ManageCourse(View):
    def get(self, request):
        return render(request, 'ManageCourse.html')

    def post(self, request):
        request.session['action'] = None
        if request.POST.get('create_button') is not None:
            request.session['action'] = 'Create'
        elif request.POST.get('edit_button') is not None:
            request.session['action'] = "Edit"
        else:
            request.session['action'] = "Delete"
        return render(request, 'ManageCourse.html')


class CreateCourse(View):
    # Only post method.
    def post(self, request):
        courseName = request.POST.get("name")
        department = request.POST.get("department")
        id = generateID(courseName)

        newCourse = Course(id = id, department= department, name=courseName)

        newCourse.save()
        return render(request, 'ManageCourse.html')


class Assigns(View):
    def get(self, request):
        if request.session.get("is_authenticate") and request.session.get('role') == "Supervisor":
            return render(request, 'Assign.html')
        else:
            return render(request, "Home.html", {"error": "DO NOT HAVE PERMISSION"})

    def post(self, request):
        pass


class Database(View):
    def get(self, request):
        return render(request, 'ViewDatabase.html')

    def post(self, request):
        pass


class LogOut(View):
    def get(self, request):
        if request.session.get('is_authenticate'):
            request.session.flush()
            # Keeping csrf_cookie fresh!
            rotate_token(request)
            response = render(request, 'login.html', {"error": "Successful Logout", "errorCSS": "successError"})
            return response
        else:
            return render(request, 'login.html', {"error": "No session can be found", "errorCSS": "failedError"})
