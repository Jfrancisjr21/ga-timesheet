from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from simple_history.admin import SimpleHistoryAdmin

from .models import User


@admin.register(User)
class UserAdmin(SimpleHistoryAdmin, BaseUserAdmin):
    list_display = ("email", "first_name", "last_name", "student_id", "is_active", "is_staff")
    search_fields = ("email", "first_name", "last_name", "student_id")
    ordering = ("email",)
    fieldsets = BaseUserAdmin.fieldsets + (
        ("GA Timesheet", {"fields": ("student_id", "onboarded_at")}),
    )
