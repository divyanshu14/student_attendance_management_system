from django.contrib import admin
from django.contrib.auth.models import User
from .models import Admin, Student, Instructor, Course, Class, CumulativeAttendance

# Register your models here.

admin.site.register(Admin)
admin.site.register(Student)
admin.site.register(Instructor)
admin.site.register(Course)
admin.site.register(Class)
admin.site.register(CumulativeAttendance)
