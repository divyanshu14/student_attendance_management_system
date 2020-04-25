from django.urls import path
from . import views

urlpatterns = [
    # auth
    path('api_token_auth/', views.obtain_auth_token, name='api_token_auth'),
    # login data
    path('get_user_data/', views.GetUserDataView.as_view(), name='get_user_data'),
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
    path('list_course/', views.ListCourseView.as_view(), name='list_course'),
    path('create_course/', views.CreateCourseView.as_view(), name='create_course'),
    path('retrieve_course/<str:code>/', views.RetrieveCourseView.as_view(), name='retrieve_course'),
    path('restricted_retrieve_course/<str:code>/', views.RestrictedRetrieveCourseView.as_view(), name='restricted_retrieve_course'),
    path('update_course/<str:code>/', views.UpdateCourseView.as_view(), name='update_course'),
    path('destroy_course/<str:code>/', views.DestroyCourseView.as_view(), name='destroy_course'),
    # class event
    path('list_class_event_for_course/<str:code>/', views.ListClassEventForCourseView.as_view(), name='list_class_event_for_course'),
    path('create_class_event_for_course/<str:code>/', views.CreateClassEventForCourseView.as_view(), name='create_class_event_for_course'),
    path('list_class_event_of_student_for_course/<str:code>/<str:entry_number>/', views.ListClassEventOfStudentForCourseView.as_view(), name='list_class_event_of_student_for_course'),
    # cumulative attendance
    path('list_cumulative_attendance_for_course/<str:code>/', views.ListCumulativeAttendanceForCourseView.as_view(), name='list_cumulative_attendance_for_course'),
    path('retrieve_cumulative_attendance_of_student_for_course/<str:code>/<str:entry_number>/', views.RetrieveCumulativeAttendanceOfStudentForCourseView.as_view(), name='retrieve_cumulative_attendance_of_student_for_course'),
]
