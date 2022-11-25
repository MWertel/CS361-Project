from django.shortcuts import render
from django.views import View
from .models import Account, Supervisor, Instructor, TA


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
