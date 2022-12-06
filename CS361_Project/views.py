from django.middleware.csrf import rotate_token
from django.shortcuts import render, redirect
from django.views import View
from .models import Account, Supervisor, Instructor, TA


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
        if request.session.get('is_authenticate'):
            return render(request, "Home.html", )
        else:
            return render(request, "login.html")


#     No Post yet.

class SupCreateAccounts(View):

    def __init__(self, name):
        pass

    def setName(self, other):
        pass

    def setEmail(self, other):
        pass

    def setID(self, other):
        pass

    def setRole(self, other):
        pass

    def setPhoneNum(self, other):
        pass

    def setAddress(self, other):
        pass


class SupEditAccounts(View):
    def __init__(self, account):
        pass

    def changeName(self, other, change):
        pass

    def changeEmail(self, other, change):
        pass

    def changeID(self, other, change):
        pass

    def changeRole(self, other, change):
        pass

    def changePhoneNum(self, other, change):
        pass

    def changeAddress(self, other):
        pass


class ManageAccounts(View):
    def get(self, request):
        return render(request, 'Accounts/Manage.html')

    def post(self, request):
        pass


class Notification(View):
    def get(self, request):
        return render(request, 'NotificationForm.html')

    def post(self, request):
        pass


class ManageCourse(View):
    def get(self, request):
        return render(request, 'ManageCourse.html')

    def post(self, request):
        pass


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
