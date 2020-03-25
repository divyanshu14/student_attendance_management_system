from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User, Group
from django.forms import formset_factory, modelformset_factory
from .forms import AddStudentForm, AddInstructorForm
from .models import Student, Instructor, Course


DEFAULT_PASSWORD = "new_pass_123"


def is_admin(user):
    '''
    Returns True if the user belongs to Admin group, otherwise returns False.
    '''
    return user.groups.filter(name='Admins').exists()


def is_student(user):
    '''
    Returns True if the user belongs to Student group, otherwise returns False.
    '''
    return user.groups.filter(name='Students').exists()


def is_instructor(user):
    '''
    Returns True if the user belongs to Instructor group, otherwise returns False.
    '''
    return user.groups.filter(name='Instructors').exists()


@login_required
@permission_required('database_manager.add_student', raise_exception=True)
def add_students(request, num_students):
    '''
    View to add students.
    '''
    AddStudentFormSet = formset_factory(
        AddStudentForm, extra=num_students)
    # if this is a POST request we need to process the formset data
    if request.method == 'POST':
        # create a formset instance and populate it with data from the request:
        formset = AddStudentFormSet(request.POST)
        # check whether it's valid:
        if formset.is_valid():
            # process the data in formset.cleaned_data as required
            for form in formset:
                user = User.objects.create_user(
                    form.cleaned_data['entry_number'], form.cleaned_data['email_address'], DEFAULT_PASSWORD)
                user.first_name = form.cleaned_data['first_name']
                user.last_name = form.cleaned_data['last_name']
                students_group = Group.objects.get(name='Students')
                user.groups.add(students_group)
                user.save()
                Student.objects.create(
                    user=user, entry_number=form.cleaned_data['entry_number'])
            # redirect to a new URL:
            message = "The students' data has been saved successfully."
            return render(request, 'database_manager/message.html', {'message': message})
    # if a GET (or any other method) we'll create a blank formset
    else:
        formset = AddStudentFormSet()

    return render(request, 'database_manager/display_formset.html', {'formset': formset})


@login_required
@permission_required('database_manager.add_instructors', raise_exception=True)
def add_instructors(request, num_instructors):
    '''
    View to add instructors.
    '''
    AddInstructorFormSet = formset_factory(
        AddInstructorForm, extra=num_instructors)
    # if this is a POST request we need to process the formset data
    if request.method == 'POST':
        # create a formset instance and populate it with data from the request:
        formset = AddInstructorFormSet(request.POST)
        # check whether it's valid:
        if formset.is_valid():
            # process the data in formset.cleaned_data as required
            for form in formset:
                user = User.objects.create_user(
                    form.cleaned_data['instructor_id'], form.cleaned_data['email_address'], DEFAULT_PASSWORD)
                user.first_name = form.cleaned_data['first_name']
                user.last_name = form.cleaned_data['last_name']
                instructors_group = Group.objects.get(name='Instructors')
                user.groups.add(instructors_group)
                user.save()
                Instructor.objects.create(
                    user=user, instructor_id=form.cleaned_data['instructor_id'])
            # redirect to a new URL:
            message = "The instructors' data has been saved successfully."
            return render(request, 'database_manager/message.html', {'message': message})
    # if a GET (or any other method) we'll create a blank formset
    else:
        formset = AddInstructorFormSet()

    return render(request, 'database_manager/display_formset.html', {'formset': formset})


@login_required
@permission_required('database_manager.add_courses', raise_exception=True)
def add_courses(request, num_courses):
    '''
    View to add courses.
    '''
    AddCourseFormSet = modelformset_factory(
        Course, extra=num_courses, exclude=())
    # if this is a POST request we need to process the formset data
    if request.method == 'POST':
        # create a formset instance and populate it with data from the request:
        formset = AddCourseFormSet(request.POST)
        # check whether it's valid:
        if formset.is_valid():
            formset.save()
            # redirect to a new URL:
            message = "The courses' data has been saved successfully."
            return render(request, 'database_manager/message.html', {'message': message})
    # if a GET (or any other method) we'll create a blank formset
    else:
        formset = AddCourseFormSet(queryset=Course.objects.none())

    return render(request, 'database_manager/display_formset.html', {'formset': formset})


@login_required
@permission_required('database_manager.add_student', raise_exception=True)
def assign_student_role_to_users(request, num_users):
    '''
    View to assign student role to users.
    Useful in cases when someone joined the institute as an instructor or admin
    (and has already been registered), but later got enrolled in some course in the institute.
    '''
    AssignStudentRoleToUsersFormset = modelformset_factory(
        Student, extra=num_users, exclude=())
    # if this is a POST request we need to process the formset data
    if request.method == 'POST':
        # create a formset instance and populate it with data from the request:
        formset = AssignStudentRoleToUsersFormset(request.POST)
        # check whether it's valid:
        if formset.is_valid():
            formset.save()
            # redirect to a new URL:
            message = "The users have been assigned the role of student successfully."
            return render(request, 'database_manager/message.html', {'message': message})
    # if a GET (or any other method) we'll create a blank formset
    else:
        formset = AssignStudentRoleToUsersFormset(queryset=Student.objects.none())

    return render(request, 'database_manager/display_formset.html', {'formset': formset})


@login_required
@permission_required('database_manager.add_instructor', raise_exception=True)
def assign_instructor_role_to_users(request, num_users):
    '''
    View to assign instructor role to users.
    Useful in cases when someone joined the institute as a student or admin
    (and has already been registered), but later became a teaching assistant or instructor in the institute.
    '''
    AssignInstructorRoleToUsersFormset = modelformset_factory(
        Instructor, extra=num_users, exclude=())
    # if this is a POST request we need to process the formset data
    if request.method == 'POST':
        # create a formset instance and populate it with data from the request:
        formset = AssignInstructorRoleToUsersFormset(request.POST)
        # check whether it's valid:
        if formset.is_valid():
            formset.save()
            # redirect to a new URL:
            message = "The users have been assigned the role of instructor successfully."
            return render(request, 'database_manager/message.html', {'message': message})
    # if a GET (or any other method) we'll create a blank formset
    else:
        formset = AssignInstructorRoleToUsersFormset(queryset=Instructor.objects.none())

    return render(request, 'database_manager/display_formset.html', {'formset': formset})
