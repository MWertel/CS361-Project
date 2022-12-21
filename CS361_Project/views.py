from django.middleware.csrf import rotate_token
from django.shortcuts import render, redirect
from django.views import View
from .models import Account, Supervisor, Instructor, TA, Course, LabSection, Course_LabSection
from .functions import generateID, changeName, changePassword, changeEmail, changeAddress,changeTelephone, passwordChecker, sendEmail, assignToTable, removeFromTable


# Create your views here.

class EditProfile(View):
    def get(self, request):
        return render(request, 'Profile/EditProfile.html')

    def post(self, request):
        name = request.POST.get("Name")
        email = request.POST.get("Email")
        phone = request.POST.get("Telephone")
        addy = request.POST.get("Address")
        curlogin = Account.objects.get(username=request.session.get("username"))
        changeName(curlogin, name)
        changeEmail(curlogin, email)
        changeTelephone(curlogin, phone)
        changeAddress(curlogin, addy)
        curlogin.save()


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
            session['username'] = user.username
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
            userList = list(Account.objects.all())
            return render(request, 'Accounts/Manage.html', {"userList": userList})
        else:
            request.session['action'] = 'delete'

        return render(request, 'Accounts/Manage.html')


class CreateAccount(View):

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

        recipients = request.POST.get('recipients').split(',')
        message = request.POST.get('message')
        sender = Account.objects.get(username = request.session.get("username")).email
        try:
            sendEmail(message, sender, recipients)
        except:
            return render(request, 'NotificationForm.html')
        return render(request, 'NotificationForm.html')


class ManageCourse(View):
    def get(self, request):
        courses = list(Course.objects.all())
        labs = list(LabSection.objects.all())
        return render(request, 'ManageCourse.html',{"courses": courses,"labs":labs})

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
            return render(request,"ManageCourse.html",{"error": error,"courses": courses, "labs": labs})

        if department == "":
            error = "Course needs a departament"
            return render(request,"ManageCourse.html",{"error": error,"courses": courses, "labs": labs})

        newCourse = Course(id = id, department= department, name=courseName)

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
            return render(request,"ManageCourse.html",{"error": error,"courses": courses, "labs": labs})

        if department == "":
            error = "Lab Section needs a department"
            return render(request,"ManageCourse.html",{"error": error,"courses": courses, "labs": labs})

        if courseName == None:
            error = "Lab Section needs to belong to a Course"
            return render(request,"ManageCourse.html", {"error": error,"courses": courses, "labs": labs})


        newLab = LabSection(id = id, department= department, name = labName)
        newLab.save()


        course = Course.objects.get(name = courseName)

        #create a join object between the two
        newJoin = Course_LabSection(labSection = newLab, course = course)
        newJoin.save()


        labs = list(LabSection.objects.all())
        return render(request, 'ManageCourse.html', {"courses": courses, "labs": labs})


class EditCourse(View):

    def post(self,request):
        courses = list(Course.objects.all())
        labs = list(LabSection.objects.all())

        if request.POST.get("course") == None:
            error = "A Course must be chosen"
            return render(request, 'ManageCourse.html', {"error": error, "courses": courses, "labs": labs})

        course = Course.objects.get(name = request.POST.get("course"))


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

    def post(self,request):
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

        course =  Course.objects.get(name = request.POST.get("course"))
        if course != None:
            oldCourseLabJoin = Course_LabSection.objects.get(lab = lab)
            oldCourseLabJoin.delete()

            newCourseLab = Course_LabSection(course=course, lab = lab)
            newCourseLab.save()


        labs = list(LabSection.objects.all())
        return render(request, 'ManageCourse.html', {"courses": courses, "labs": labs})

class DeleteCourse(View):

    def post(self,request):
        courses = list(Course.objects.all())
        labs = list(LabSection.objects.all())
        if request.POST.get("course") != None:
            course = Course.objects.get(id = request.POST.get("course"))

            #Delete all within the Join List
            joinList = list(Course_LabSection.objects.filter(course = course))

            for l in joinList:
                l.labSection.delete()

            course.delete()

            courses = list(Course.objects.all())
            labs = list(LabSection.objects.all())
            return render(request, 'ManageCourse.html', {"courses": courses, "labs": labs})

        error = "No Course was selected"
        return render(request,"ManageCourse.html",{"error":error,"courses": courses, "labs": labs})


class DeleteLab(View):

    def post(self, request):
        courses = list(Course.objects.all())
        labs = list(LabSection.objects.all())

        if request.POST.get("lab") is not None:
            lab = LabSection.objects.get(id = request.POST.get("lab"))
            lab.delete()

            labs = list(LabSection.objects.all())
            return render(request, 'ManageCourse.html', {"courses": courses, "labs": labs})

        error = "No Lab Section was selected"
        return render(request, "ManageCourse.html", {"error": error,"courses": courses, "labs": labs})


class ManageAssign(View):
    def get(self, request):
        if request.session.get("is_authenticate") and request.session.get('role') == "Supervisor":
            courses = list(Course.objects.all())
            labs = list(LabSection.objects.all())

            users = list(Account.objects.filter(role = "TA")) + list(Account.objects.filter(role = "Instructor"))

            return render(request, 'Assign.html',{"selectedUsers":users,"courses":courses,"labs":labs})
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

            user = Account.objects.get(username = username)
            if not assignToTable(user,course.labSection):#Failure to assign due to assignment already existing
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
