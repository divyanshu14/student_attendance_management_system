from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import url
from django.urls import include
from rest_framework import routers
from rest_framework.authtoken import views as authViews

router = routers.DefaultRouter()
router.register(r'add_students', views.addStudents, basename='add_students')
router.register(r'add_instructors', views.addInstructors, basename='add_instructors')
router.register(r'add_teaching_assistant', views.addTeachingAssistant, basename='add_instructors')
# router.register(r'list_teaching_assistant', views.listTeachingAssistant, basename='list_teaching_assistant')
router.register(r'assign_student_to_user', views.assignStudentToUser, basename='assign_user_to_student')
router.register(r'assign_instructor_to_user', views.assignInstructorToUser, basename='assign_user_to_instructor')
router.register(r'assign_instructor_to_class_event_coordinator', views.assignInstructorToClassEventCoordinator, basename='assign_instructor_to_class_event_coordinator')
router.register(r'assign_teaching_assistant_to_user', views.assignTeachingAssistantToUser, basename='assign_teaching_assistant_to_user')
router.register(r'assign_teaching_assistant_to_class_event_coordinator', views.assignTeachingAssistantToClassEventCoordinator, basename='assign_teaching_assistant_to_class_event_coordinator')
# router.register(r'list_courses', views.listCourses, basename='list_courses')
router.register(r'add_courses', views.addCourses, basename='add_courses')

urlpatterns = [
    url(r'', include(router.urls)),
    path('list_students/', views.listStudents.as_view(), name='list_students'),
    path('list_instructors/', views.listInstructors.as_view(), name='list_instructors'),
    # path('add_courses', views.addCourses.as_view(), name='add_courses'),
    path('list_courses', views.listCourses.as_view(), name='list_courses'),
    path('list_teaching_assistant', views.listTeachingAssistant.as_view(), name='list_teaching_assistant'),
    url(r'^login/', authViews.obtain_auth_token)
]


# #...
