
from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import url
from django.urls import include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'add_students', addStudents, basename='add_students')
router.register(r'add_instructors', addInstructors, basename='add_instructors')
router.register(r'add_course', addCourses, basename='add_courses')
router.register(r'assign_user_to_student', assignUserToStudent, basename='assign_user_to_student')
router.register(r'assign_user_to_instructor', assignUserToInstructor, basename='assign_user_to_instructor')

urlpatterns = [
    url(r'', include(router.urls)),
    # path('add_students/<int:num_students>', views.ThingViewSet.as_view(), name='add_students'),
    path('list_students/', views.listStudents.as_view(), name='list_students'),
    path('list_instructors/', views.listInstructors.as_view(), name='list_instructors'),
    # path('api/v1/add_instructors/<int:num_instructors>', views.add_instructors, name='add_instructors'),
    # path('api/v1/add_courses/<int:num_courses>', views.add_courses, name='add_courses'),
    # path('api/v1/assign_student_role_to_users/<int:num_users>', views.assign_student_role_to_users, name='assign_student_role_to_users'),
    # path('api/v1/assign_instructor_role_to_users/<int:num_users>', views.assign_instructor_role_to_users, name='assign_instructor_role_to_users'),
]


# #...
