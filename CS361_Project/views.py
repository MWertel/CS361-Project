from django.shortcuts import render
from django.views import View
from django.db.utils import OperationalError
from .models import Account, Supervisor


# Create your views here.

class Login(View):
    def get(self, request):
        return render(request, "login.html", {})

    # Have not implemented redirect (Waiting for redirect necessary html)
    def post(self, request):
        wrongPassword = False
        try:
            user = Account.objects.get(username=request.POST['username'])
            wrongPassword = (user.password != request.POST['password'])
        except Account.DoesNotExist:
            return render(request, "login.html", {"error": "User doesn't exist"})
        except OperationalError as OE:
            return render(request, "login.html",{"error": "No account is found"})
        if wrongPassword:
            return render(request, "login.html", {"error": "Incorrect password"})
        # redirect to "Manage Account"
            # Depend on the requirement, account will have access to certain button.