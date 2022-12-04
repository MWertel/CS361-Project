from django.shortcuts import render
from django.views import View
from .models import Account, Supervisor


# Create your views here.

class Login(View):
    def get(self, request):
        return render(request, "login.html", {})

    # Have not implemented redirect (Waiting for redirect necessary html)
    def post(self, request):
        wrongPassword = False
        try:
            user = Account.objects.get(username=request.POST['Username'])
            wrongPassword = (user.password != request.POST['Password'])
        except Account.DoesNotExist:
            return render(request, "login.html", {"error": "User doesn't exist"})
        if wrongPassword:
            return render(request, "login.html", {"error": "Incorrect password"})
        # else . . . -> Redirect.
        # Pseudo Codes
        # user.role == Supervisor:
        # return redirect("/admin/")
        # elif user.role == Instructor
        # return redirect("/instructor/")
        # elif user.role == TA
        # return redirect("/ta/")


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
