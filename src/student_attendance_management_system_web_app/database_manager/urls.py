from django.urls import path
from . import views

urlpatterns = [
    path('add_students/<int:num_students>/', views.add_students, name='add_students'),
    path('add_instructors/<int:num_instructors>/', views.add_instructors, name='add_instructors'),
    path('add_teaching_assistants/<int:num_teaching_assistants>/', views.add_teaching_assistants, name='add_teaching_assistants'),
    path('add_courses/<int:num_courses>/', views.add_courses, name='add_courses'),
    path('assign_student_role_to_users/<int:num_users>/', views.assign_student_role_to_users, name='assign_student_role_to_users'),
    path('assign_instructor_role_to_users/<int:num_users>/', views.assign_instructor_role_to_users, name='assign_instructor_role_to_users'),
    path('assign_instructor_role_to_class_event_coordinators/<int:num_class_event_coordinators>/', views.assign_instructor_role_to_class_event_coordinators, name='assign_instructor_role_to_class_event_coordinators'),
    path('assign_teaching_assistant_role_to_users/<int:num_users>/', views.assign_teaching_assistant_role_to_users, name='assign_teaching_assistant_role_to_users'),
    path('assign_teaching_assistant_role_to_class_event_coordinators/<int:num_class_event_coordinators>/', views.assign_teaching_assistant_role_to_class_event_coordinators, name='assign_teaching_assistant_role_to_class_event_coordinators'),
    path('view_course_attendance_details/<int:course_id>/', views.view_course_attendance_details, name='view_course_attendance_details'),
    path('view_student_attendance_details_in_a_course/<int:course_id>/<int:student_id>/', views.view_student_attendance_details_in_a_course, name='view_student_attendance_details_in_a_course'),
]
