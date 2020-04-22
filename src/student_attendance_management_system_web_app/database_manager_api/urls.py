from django.urls import path
from . import views

urlpatterns = [
    # auth
    path('api_token_auth/', views.obtain_auth_token, name='api_token_auth'),
    # student
    path('list_create_student_user/', views.ListCreateStudentUserView.as_view(), name='list_create_student_user'),
    path('retrieve_update_destroy_student_user/<str:entry_number>/', views.RetrieveUpdateDestroyStudentUserView.as_view(), name='retrieve_update_destroy_student_user'),
    path('create_student/', views.CreateStudentView.as_view(), name='create_student'),
    # instructor
    path('list_create_instructor_class_event_coordinator_user/', views.ListCreateInstructorClassEventCoordinatorUserView.as_view(), name='list_create_instructor_class_event_coordinator_user'),
    path('retrieve_update_destroy_instructor_class_event_coordinator_user/<str:instructor_id>/', views.RetrieveUpdateDestroyInstructorClassEventCoordinatorUserView.as_view(), name='retrieve_update_destroy_instructor_class_event_coordinator_user'),
    path('create_instructor/', views.CreateInstructorView.as_view(), name='create_instructor'),
    # teaching assistant
    path('list_create_teaching_assistant_class_event_coordinator_user/', views.ListCreateTeachingAssistantClassEventCoordinatorUserView.as_view(), name='list_create_teaching_assistant_class_event_coordinator_user'),
    path('retrieve_update_destroy_teaching_assistant_class_event_coordinator_user/<str:teaching_assistant_id>/', views.RetrieveUpdateDestroyTeachingAssistantClassEventCoordinatorUserView.as_view(), name='retrieve_update_destroy_teaching_assistant_class_event_coordinator_user'),
    path('create_teaching_assistant/', views.CreateTeachingAssistantView.as_view(), name='create_teaching_assistant'),
    # course
    path('list_create_course/', views.ListCreateCourseView.as_view(), name='list_create_course'),
    path('retrieve_update_destroy_course/<str:code>/', views.RetrieveUpdateDestroyCourseView.as_view(), name='retrieve_update_destroy_course'),
    # class event
    path('list_class_event_for_course/<str:code>/', views.ListClassEventForCourseView.as_view(), name='list_class_event_for_course'),
    path('create_class_event_for_course/<str:code>/', views.CreateClassEventForCourseView.as_view(), name='create_class_event_for_course'),
]
