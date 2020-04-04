from django.shortcuts import render, redirect
from registration.forms import (
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
    if request.method == 'POST':
        if 'Add Students-num_students_to_add' in request.POST:
            num_students_to_add_form = NumStudentsToAddForm(request.POST, prefix='Add Students')
            num_instructors_to_add_form = NumInstructorsToAddForm(prefix='Add Instructors')
            num_courses_to_add_form = NumCoursesToAddForm(prefix='Add Courses')
            num_teaching_assistants_to_add_form = NumTeachingAssistantsToAddForm(prefix='Add Teaching Assistants')
            if num_students_to_add_form.is_valid():
                return redirect('add_students', num_students=num_students_to_add_form.cleaned_data['num_students_to_add'], permanent=True)
        elif 'Add Instructors-num_instructors_to_add' in request.POST:
            num_students_to_add_form = NumStudentsToAddForm(prefix='Add Students')
            num_instructors_to_add_form = NumInstructorsToAddForm(request.POST, prefix='Add Instructors')
            num_courses_to_add_form = NumCoursesToAddForm(prefix='Add Courses')
            num_teaching_assistants_to_add_form = NumTeachingAssistantsToAddForm(prefix='Add Teaching Assistants')
            if num_instructors_to_add_form.is_valid():
                return redirect('add_instructors', num_instructors=num_instructors_to_add_form.cleaned_data['num_instructors_to_add'], permanent=True)
        elif 'Add Courses-num_courses_to_add' in request.POST:
            num_students_to_add_form = NumStudentsToAddForm(prefix='Add Students')
            num_instructors_to_add_form = NumInstructorsToAddForm(prefix='Add Instructors')
            num_courses_to_add_form = NumCoursesToAddForm(request.POST, prefix='Add Courses')
            num_teaching_assistants_to_add_form = NumTeachingAssistantsToAddForm(prefix='Add Teaching Assistants')
            if num_courses_to_add_form.is_valid():
                return redirect('add_courses', num_courses=num_courses_to_add_form.cleaned_data['num_courses_to_add'], permanent=True)
        elif 'Add Teaching Assistants-num_teaching_assistants_to_add' in request.POST:
            num_students_to_add_form = NumStudentsToAddForm(prefix='Add Students')
            num_instructors_to_add_form = NumInstructorsToAddForm(prefix='Add Instructors')
            num_courses_to_add_form = NumCoursesToAddForm(prefix='Add Courses')
            num_teaching_assistants_to_add_form = NumTeachingAssistantsToAddForm(request.POST, prefix='Add Teaching Assistants')
            if num_teaching_assistants_to_add_form.is_valid():
                return redirect('add_teaching_assistants', num_teaching_assistants=num_teaching_assistants_to_add_form.cleaned_data['num_teaching_assistants_to_add'], permanent=True)
    else:
        num_students_to_add_form = NumStudentsToAddForm(prefix='Add Students')
        num_instructors_to_add_form = NumInstructorsToAddForm(prefix='Add Instructors')
        num_courses_to_add_form = NumCoursesToAddForm(prefix='Add Courses')
        num_teaching_assistants_to_add_form = NumTeachingAssistantsToAddForm(prefix='Add Teaching Assistants')

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
        'num_students_to_add_form': num_students_to_add_form,
        'num_instructors_to_add_form': num_instructors_to_add_form,
        'num_courses_to_add_form': num_courses_to_add_form,
        'num_teaching_assistants_to_add_form': num_teaching_assistants_to_add_form,
        'registered_student_for_courses': registered_student_for_courses,
        'instructor_for_courses': instructor_for_courses,
        'teaching_assistant_for_courses': teaching_assistant_for_courses
    }
    return render(request, 'profile.html', context)
