from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from Employees.models import Employee

class ProfileInline(admin.StackedInline):
    model = Employee
    fk_name = 'account'
    max_num = 1


class CustomUserAdmin(UserAdmin):
    inlines = [ProfileInline,]


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
