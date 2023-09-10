from django.contrib import admin
from .models import MugDepartment, Timetable
# Register your models here.
@admin.register(MugDepartment)
class MugDepartmentAdmin(admin.ModelAdmin):
    list_display = ['departmentName', 'created_at','updated_at'
                    ]


@admin.register(Timetable)
class Timetable(admin.ModelAdmin):
    list_display = [
        "name",
        "department",
        "timetableDoc",
        "updated_at"
    ]