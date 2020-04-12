from django.shortcuts import render, redirect
from .forms import (
    NumStudentsToAddForm,
    NumInstructorsToAddForm,
    NumTeachingAssistantsToAddForm,
    NumCoursesToAddForm,
)
from database_manager.models import Course


def index(request):
    return render(request, 'index.html')


def team(request):
    return render(request, 'team.html')


def about(request):
    return render(request, 'about.html')


def profile(request):
    is_admin = hasattr(request.user, 'admin')
    is_student = hasattr(request.user, 'student')
    is_classeventcoordinator = hasattr(request.user, 'classeventcoordinator')
    if is_classeventcoordinator:
        is_instructor = hasattr(request.user.classeventcoordinator, 'instructor')
        is_teachingassistant = hasattr(request.user.classeventcoordinator, 'teachingassistant')
        # is_labattendant = hasattr(request.user.classeventcoordinator, 'labattendant')
    else:
        is_instructor = False
        is_teachingassistant = False
        # is_labattendant = False

    if is_student:
        registered_student_for_courses = request.user.student.course_set.all()
    else:
        registered_student_for_courses = Course.objects.none()

    if is_instructor:
        instructor_for_courses = request.user.classeventcoordinator.instructor.course_set.all()
    else:
        instructor_for_courses = Course.objects.none()

    if is_teachingassistant:
        teaching_assistant_for_courses = request.user.classeventcoordinator.teachingassistant.course_set.all()
    else:
        teaching_assistant_for_courses = Course.objects.none()

    context = {
        'is_admin': is_admin,
        'is_student': is_student,
        'is_classeventcoordinator': is_classeventcoordinator,
        'is_instructor': is_instructor,
        'is_teachingassistant': is_teachingassistant,
        # 'is_labattendant': is_labattendant,
        'registered_student_for_courses': registered_student_for_courses,
        'instructor_for_courses': instructor_for_courses,
        'teaching_assistant_for_courses': teaching_assistant_for_courses
    }
    return render(request, 'profile.html', context)
