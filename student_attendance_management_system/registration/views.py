from django.shortcuts import render, redirect
from .forms import NumStudentsToAddForm, NumInstructorsToAddForm, NumCoursesToAddForm


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
            if num_students_to_add_form.is_valid():
                return redirect('add_students', num_students=num_students_to_add_form.cleaned_data['num_students_to_add'], permanent=True)
        elif 'Add Instructors-num_instructors_to_add' in request.POST:
            num_students_to_add_form = NumStudentsToAddForm(prefix='Add Students')
            num_instructors_to_add_form = NumInstructorsToAddForm(request.POST, prefix='Add Instructors')
            num_courses_to_add_form = NumCoursesToAddForm(prefix='Add Courses')
            if num_instructors_to_add_form.is_valid():
                return redirect('add_instructors', num_instructors=num_instructors_to_add_form.cleaned_data['num_instructors_to_add'], permanent=True)
        elif 'Add Courses-num_courses_to_add' in request.POST:
            num_students_to_add_form = NumStudentsToAddForm(prefix='Add Students')
            num_instructors_to_add_form = NumInstructorsToAddForm(prefix='Add Instructors')
            num_courses_to_add_form = NumCoursesToAddForm(request.POST, prefix='Add Courses')
            if num_courses_to_add_form.is_valid():
                return redirect('add_courses', num_courses=num_courses_to_add_form.cleaned_data['num_courses_to_add'], permanent=True)
    else:
        num_students_to_add_form = NumStudentsToAddForm(prefix='Add Students')
        num_instructors_to_add_form = NumInstructorsToAddForm(prefix='Add Instructors')
        num_courses_to_add_form = NumCoursesToAddForm(prefix='Add Courses')

    is_admin = hasattr(request.user, 'admin')
    is_student = hasattr(request.user, 'student')
    is_instructor = hasattr(request.user, 'instructor')

    registered_student_for_courses = request.user.registered_student_for_courses.all()
    instructor_for_courses = request.user.instructor_for_courses.all()
    teaching_assistant_for_courses = request.user.teaching_assistant_for_courses.all()

    context = {'is_admin': is_admin, 'is_student': is_student, 'is_instructor': is_instructor,
        'num_students_to_add_form': num_students_to_add_form,
        'num_instructors_to_add_form': num_instructors_to_add_form,
        'num_courses_to_add_form': num_courses_to_add_form,
        'registered_student_for_courses': registered_student_for_courses,
        'instructor_for_courses': instructor_for_courses,
        'teaching_assistant_for_courses': teaching_assistant_for_courses}
    return render(request, 'profile.html', context)
