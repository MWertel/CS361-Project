from django.contrib import admin
from .models import Account, Supervisor, Instructor, TA

admin.site.register(Account)
admin.site.register(Supervisor)
admin.site.register(Instructor)
admin.site.register(TA)

