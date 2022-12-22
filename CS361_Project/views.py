from django.middleware.csrf import rotate_token
from django.shortcuts import render
from django.views import View

from SuperLooper.auth import *
from .models import *
from SuperLooper.functions import *


# Create your views here.

class Login(View):
    def get(self, request):
        return checkAuthentication(request)

    def post(self, request):
        try:
            request.session = login(request)
        except ValueError as error:
            return errorRender(request, 'login', error)
        return redirectSession(request)


class Profile(View):

    def get(self, request):
        request.session['action'] = None
        return render(request, 'Profile.html', {"validForm": "invalid"})

    def post(self, request):
        request.session['action'] = None
        if request.POST.get('editProfile') is not None:
            request.session['action'] = 'edit'
        elif request.POST.get('changePassword') is not None:
            request.session['action'] = "changePassword"
        return render(request, 'Profile.html')

class EditProfile(View):
    def get(self, request):
        return render(request, 'Profile.html', {"validForm": "valid"})

    def post(self, request):
        username = request.session['user']["username"]

        editAccount = Account.objects.get(username=username)
        currPassword = request.POST.get("CurrentPassword")

        if currPassword != "":
            if currPassword != editAccount.password:
                #error = {"error": "Current password doesn't match existing one"}
                #errorRender(request,"Profile",context= ValueError(error))
                error = "Current Password doesn't match with the user's"
                return render(request, "Profile.html", {"error": error})

            if passwordChecker(request.POST.get("NewPassword")) == False:  # Bad Password
                error = "New Password must have at least one digit, one upper case character, one lower case character, one special symbol, and at least 5 characters"
                return render(request, "Profile.html", {"error": error})


            if request.POST.get("NewPassword") != request.POST.get("NewPasswordRepeat"):
                error = "Passwords don't match"
                return render(request, "Profile.html", {"error": error})

            changePassword(editAccount, request.POST.get("Password"))

        if request.POST.get("Email") != "":
            changeEmail(editAccount, request.POST.get("Email"))

        if request.POST.get("Telephone") != "":
            changeTelephone(editAccount, request.POST.get("Telephone"))

        if request.POST.get("Address") != "":
            changeAddress(editAccount, request.POST.get("Address"))

        editAccount.save()
        return render(request, 'Profile.html')

class Home(View):
    def get(self, request):
        return checkAuthentication(request)
#     No Post yet.


class ManageAccounts(View):
    def get(self, request):
        request.session['action'] = None
        return render(request, 'Manage.html', {"validForm": 'invalid'})

    def post(self, request):
        userList = list(Account.objects.all())
        request.session['action'] = None
        if request.POST.get('create') is not None:
            request.session['action'] = 'create'
        elif request.POST.get('edit') is not None:
            request.session['action'] = 'edit'
            return render(request, 'Manage.html', {"userList": userList})
        else:
            request.session['action'] = 'delete'

        return render(request, 'Manage.html',{"userList": userList})


class CreateAccount(View):

    def post(self, request):
        action = request.session["action"]
        users = list(Account.objects.all())
        if action == "create":
            username = request.POST.get("Username")
            if len(list(Account.objects.filter(username=username))) > 0:  # username already exists
                error = "Username already exists in Database"
                return render(request, 'Manage.html', {"error": error,"userList":users})

            role = request.POST.get("role")
            if role == None:  # No role given, the user requires a role
                error = "Every user needs to have a role"
                return render(request, "Manage.html", {"error": error,"userList":users})

            password = request.POST.get("Password")
            if passwordChecker(password) == False:  # Bad Password
                error = "Password must have at least one digit, one upper case character, one lower case character, one special symbol, and at least 5 characters"
                return render(request, "Manage.html", {"error": error,"userList":users})

            id = generateID(username)
            newAccount = Account(id=id, username=username,
                                 password=password,
                                 name=request.POST.get("Name"),
                                 role=role,
                                 email=request.POST.get("Email"),
                                 telephone=request.POST.get("Telephone"),
                                 address=request.POST.get("Address")
                                 )
            newAccount.save()

        return render(request, 'Manage.html', {"userList":users})


class EditAccount(View):

    def post(self, request):
        users = list(Account.objects.all())
        action = request.session["action"]
        if action == "edit":

            username = request.POST.get("Username")
            if len(list(Account.objects.filter(username=username))) == 0:  # username doesn't exists
                error = "Username not in Database"
                return render(request, 'Manage.html', {"error": error,"userList":users})

            editAccount = Account.objects.get(username=username)
            if request.POST.get("Password") != "":
                if passwordChecker(request.POST.get("Password")) == False:  # Bad Password
                    error = "Password must have at least one digit, one upper case character, one lower case character, one special symbol, and at least 5 characters"
                    return render(request, "Manage.html", {"error": error,"userList":users})
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

        users = list(Account.objects.all())
        return render(request, 'Manage.html',{"userList":users})


class DeleteAccount(View):

    def post(self, request):
        users = list(Account.objects.all())
        action = request.session["action"]

        if action == "delete":  # delete
            username = request.POST.get("Username")
            if len(list(Account.objects.filter(username=username))) == 0:  # username doesn't exists
                error = "Username not in Database"
                return render(request, 'Manage.html', {"error": error, "userList":users})
            else:
                deleteAccount = Account.objects.get(username=username)
                deleteAccount.delete()

        users = list(Account.objects.all())
        return render(request, 'Manage.html',{"userList":users})


class Notification(View):
    def get(self, request):
        return render(request, 'NotificationForm.html')

    def post(self, request):

        recipients = request.POST.get('recipients').split(',')
        message = request.POST.get('message')
        sender = Account.objects.get(username=request.session.get("username")).email
        try:
            sendEmail(message, sender, recipients)
        except:
            return render(request, 'NotificationForm.html')
        return render(request, 'NotificationForm.html')


class ManageCourse(View):
    def get(self, request):
        courses = list(Course.objects.all())
        labs = list(LabSection.objects.all())
        return render(request, 'ManageCourse.html', {"courses": courses, "labs": labs})

    def post(self, request):
        request.session['action'] = None
        if request.POST.get('create_button') is not None:
            request.session['action'] = 'Create'
        elif request.POST.get("createLab_button") is not None:
            request.session['action'] = "Create_Lab"
        elif request.POST.get('edit_button') is not None:
            request.session['action'] = "Edit"
        elif request.POST.get("editLab_button") is not None:
            request.session['action'] = "Edit_Lab"
        elif request.POST.get("delete_button") is not None:
            request.session['action'] = "Delete"
        else:
            request.session['action'] = "Delete_Lab"

        courses = list(Course.objects.all())
        labs = list(LabSection.objects.all())
        return render(request, 'ManageCourse.html', {"courses": courses, "labs": labs})


class CreateCourse(View):
    # Only post method.
    def post(self, request):
        courses = list(Course.objects.all())
        labs = list(LabSection.objects.all())

        courseName = request.POST.get("name")
        department = request.POST.get("department")
        id = generateID(courseName)

        if courseName == "":
            error = "Name of the Course cannot be empty"
            return render(request, "ManageCourse.html", {"error": error, "courses": courses, "labs": labs})

        if department == "":
            error = "Course needs a departament"
            return render(request, "ManageCourse.html", {"error": error, "courses": courses, "labs": labs})

        newCourse = Course(id=id, department=department, name=courseName)

        newCourse.save()

        courses = list(Course.objects.all())
        return render(request, 'ManageCourse.html', {"courses": courses, "labs": labs})


class CreateLab(View):
    def post(self, request):
        courses = list(Course.objects.all())
        labs = list(LabSection.objects.all())

        labName = request.POST.get("name")
        department = request.POST.get("department")
        id = generateID(labName)
        courseName = request.POST.get("course")

        if labName == "":
            error = "Name of the Lab Section cannot be empty"
            return render(request, "ManageCourse.html", {"error": error, "courses": courses, "labs": labs})

        if department == "":
            error = "Lab Section needs a department"
            return render(request, "ManageCourse.html", {"error": error, "courses": courses, "labs": labs})

        if courseName == None:
            error = "Lab Section needs to belong to a Course"
            return render(request, "ManageCourse.html", {"error": error, "courses": courses, "labs": labs})

        newLab = LabSection(id=id, department=department, name=labName)
        newLab.save()

        course = Course.objects.get(name=courseName)

        # create a join object between the two
        newJoin = Course_LabSection(labSection=newLab, course=course)
        newJoin.save()

        labs = list(LabSection.objects.all())
        return render(request, 'ManageCourse.html', {"courses": courses, "labs": labs})


class EditCourse(View):

    def post(self, request):
        courses = list(Course.objects.all())
        labs = list(LabSection.objects.all())

        if request.POST.get("course") == None:
            error = "A Course must be chosen"
            return render(request, 'ManageCourse.html', {"error": error, "courses": courses, "labs": labs})

        course = Course.objects.get(name=request.POST.get("course"))

        courseName = request.POST.get("name")
        if courseName != "":
            course.name = courseName

        department = request.POST.get("department")
        if department != "":
            course.department = department

        course.save()

        courses = list(Course.objects.all())
        return render(request, 'ManageCourse.html', {"courses": courses, "labs": labs})


class EditLab(View):

    def post(self, request):
        courses = list(Course.objects.all())
        labs = list(LabSection.objects.all())

        if request.POST.get("lab") == None:
            error = "A Lab Section must be chosen"
            return render(request, 'ManageCourse.html', {"error": error, "courses": courses, "labs": labs})

        lab = LabSection.objects.get(name=request.POST.get("lab"))

        newName = request.POST.get("name")
        if newName != "":
            lab.name = newName

        newDepartment = request.POST.get("department")
        if newDepartment != "":
            lab.department = newDepartment

        lab.save()

        course = Course.objects.get(name=request.POST.get("course"))
        if course != None:
            oldCourseLabJoin = Course_LabSection.objects.get(lab=lab)
            oldCourseLabJoin.delete()

            newCourseLab = Course_LabSection(course=course, lab=lab)
            newCourseLab.save()

        labs = list(LabSection.objects.all())
        return render(request, 'ManageCourse.html', {"courses": courses, "labs": labs})


class DeleteCourse(View):

    def post(self, request):
        courses = list(Course.objects.all())
        labs = list(LabSection.objects.all())
        if request.POST.get("course") != None:
            course = Course.objects.get(id=request.POST.get("course"))

            # Delete all within the Join List
            joinList = list(Course_LabSection.objects.filter(course=course))

            for l in joinList:
                l.labSection.delete()

            course.delete()

            courses = list(Course.objects.all())
            labs = list(LabSection.objects.all())
            return render(request, 'ManageCourse.html', {"courses": courses, "labs": labs})

        error = "No Course was selected"
        return render(request, "ManageCourse.html", {"error": error, "courses": courses, "labs": labs})


class DeleteLab(View):

    def post(self, request):
        courses = list(Course.objects.all())
        labs = list(LabSection.objects.all())

        if request.POST.get("lab") is not None:
            lab = LabSection.objects.get(id=request.POST.get("lab"))
            lab.delete()

            labs = list(LabSection.objects.all())
            return render(request, 'ManageCourse.html', {"courses": courses, "labs": labs})

        error = "No Lab Section was selected"
        return render(request, "ManageCourse.html", {"error": error, "courses": courses, "labs": labs})


class ManageAssign(View):
    def get(self, request):
        if request.session.get("is_authenticate") and request.session.get('role') == "Supervisor":
            courses = list(Course.objects.all())
            labs = list(LabSection.objects.all())

            users = list(Account.objects.filter(role="TA")) + list(Account.objects.filter(role="Instructor"))

            return render(request, 'Assign.html', {"selectedUsers": users, "courses": courses, "labs": labs})
        else:
            return render(request, "Home.html", {"error": "DO NOT HAVE PERMISSION"})

    def post(self, request):
        request.session['action'] = None
        courses = list(Course.objects.all())
        labs = list(LabSection.objects.all())
        users = list(Account.objects.filter(role="TA")) + list(Account.objects.filter(role="Instructor"))

        if request.POST.get('assign_button') is not None:
            request.session['action'] = 'Assign'
        else:
            request.session['action'] = "Remove"

        return render(request, 'Assign.html', {"selectedUsers": users, "courses": courses, "labs": labs})


class AssignUser(View):
    def get(self, request):
        return render(request, 'Assign.html')

    def post(self, request):
        action = request.session["action"]

        if action == "Assign":
            username = request.POST.get("user")

            if username == None:
                error = "There needs to be an user to assign Course and/or Lab Section"
                return render(request, 'Assign.html', {"error": error})

            course = request.POST.get("course")
            labSection = request.POST.get("lab")

            if course == None and labSection == None:
                error = "There needs to be a course or labsection to assign user to"
                return render(request, 'Assign.html', {"error": error})

            user = Account.objects.get(username=username)
            if not assignToTable(user, course.labSection):  # Failure to assign due to assignment already existing
                error = "User was already assigned to Course-Lab Section Combination"
                return render(request, 'Assign.html', {"error": error})

        return render(request, 'Assign.html')


class RemoveAssign(View):
    def get(self, request):
        return render(request, 'Assign.html')

    def post(self, request):
        action = request.session["action"]
        if action == "Remove":
            action = request.session["action"]

            username = request.POST.get("user")

            if username == None:
                error = "There needs to be an user to remove Course and/or Lab Section assignment"
                return render(request, 'Assign.html', {"error": error})

            course = request.POST.get("course")
            labSection = request.POST.get("lab")

            if course == None and labSection == None:
                error = "There needs to be a course or labs ection to remove user from"
                return render(request, 'Assign.html', {"error": error})

            user = Account.objects.get(username=username)
            removeFromTable(user, course.labSection)
        return render(request, 'Assign.html')

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
