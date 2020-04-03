from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Group
from django.forms import formset_factory, modelformset_factory
from .forms import AddStudentForm, AddInstructorForm
from .models import Student, Instructor, Course, ClassEvent
from django.core.exceptions import PermissionDenied
from django.conf import settings


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


def is_teaching_assistant(user):
    '''
    Returns True if the user belongs to Teaching Assistant group, otherwise returns False.
    '''
    return user.groups.filter(name='Teaching Assistants').exists()


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
                user = settings.AUTH_USER_MODEL.objects.create_user(form.cleaned_data['email_address'],
                    DEFAULT_PASSWORD
                )
                user.first_name = form.cleaned_data['first_name']
                user.last_name = form.cleaned_data['last_name']
                user.save()
                Student.objects.create(user=user, entry_number=form.cleaned_data['entry_number'])
            # show success message
            message = "The students' data has been saved successfully."
            return render(request, 'database_manager/message.html', {'message': message})
    # if a GET (or any other method) we'll create a blank formset
    else:
        formset = AddStudentFormSet()

    title = "Add Students"
    return render(request, 'database_manager/display_formset.html', {'title': title, 'formset': formset})


@login_required
@permission_required('database_manager.add_instructor', raise_exception=True)
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
                user = settings.AUTH_USER_MODEL.objects.create_user(form.cleaned_data['email_address'],
                    DEFAULT_PASSWORD
                )
                user.first_name = form.cleaned_data['first_name']
                user.last_name = form.cleaned_data['last_name']
                user.save()
                Instructor.objects.create(user=user, instructor_id=form.cleaned_data['instructor_id'])
            # show success message
            message = "The instructors' data has been saved successfully."
            return render(request, 'database_manager/message.html', {'message': message})
    # if a GET (or any other method) we'll create a blank formset
    else:
        formset = AddInstructorFormSet()

    title = "Add Instructors"
    return render(request, 'database_manager/display_formset.html', {'title': title, 'formset': formset})


@login_required
@permission_required('database_manager.add_course', raise_exception=True)
def add_courses(request, num_courses):
    '''
    View to add courses.
    '''
    AddCourseFormSet = modelformset_factory(
        Course, extra=num_courses, fields=(
            'name', 'code', 'relative_attendance_for_one_lecture',
            'relative_attendance_for_one_tutorial', 'relative_attendance_for_one_practical',
            'instructors', 'teaching_assistants', 'registered_students'
            )
        )
    # if this is a POST request we need to process the formset data
    if request.method == 'POST':
        # create a formset instance and populate it with data from the request:
        formset = AddCourseFormSet(request.POST)
        # check whether it's valid:
        if formset.is_valid():
            # This calls Course.save() method for each form entry
            # and does not behave the same as saving a queryset all at once
            formset.save()
            # show success message
            message = "The courses' data has been saved successfully."
            return render(request, 'database_manager/message.html', {'message': message})
    # if a GET (or any other method) we'll create a blank formset
    else:
        formset = AddCourseFormSet(queryset=Course.objects.none())

    title = "Add Courses"
    return render(request, 'database_manager/display_formset.html', {'title': title, 'formset': formset})


@login_required
@permission_required('database_manager.add_student', raise_exception=True)
def assign_student_role_to_users(request, num_users):
    '''
    View to assign student role to users.
    Useful in cases when someone joined the institute as an instructor or admin
    (and has already been registered), but later got enrolled in some course in the institute.
    '''
    AssignStudentRoleToUsersFormset = modelformset_factory(
        Student, extra=num_users, fields=('user', 'entry_number'))
    # if this is a POST request we need to process the formset data
    if request.method == 'POST':
        # create a formset instance and populate it with data from the request:
        formset = AssignStudentRoleToUsersFormset(request.POST)
        # check whether it's valid:
        if formset.is_valid():
            # This calls Student.save() method for each form entry
            # and does not behave the same as saving a queryset all at once
            formset.save()
            # show success message
            message = "The users have been assigned the role of student successfully."
            return render(request, 'database_manager/message.html', {'message': message})
    # if a GET (or any other method) we'll create a blank formset
    else:
        formset = AssignStudentRoleToUsersFormset(queryset=Student.objects.none())

    title = "Assign Student role to Users"
    return render(request, 'database_manager/display_formset.html', {'title': title, 'formset': formset})


@login_required
@permission_required('database_manager.add_instructor', raise_exception=True)
def assign_instructor_role_to_users(request, num_users):
    '''
    View to assign instructor role to users.
    Useful in cases when someone joined the institute as a student or admin
    (and has already been registered), but later became a teaching assistant or instructor in the institute.
    '''
    AssignInstructorRoleToUsersFormset = modelformset_factory(
        Instructor, extra=num_users, fields=('user', 'instructor_id'))
    # if this is a POST request we need to process the formset data
    if request.method == 'POST':
        # create a formset instance and populate it with data from the request:
        formset = AssignInstructorRoleToUsersFormset(request.POST)
        # check whether it's valid:
        if formset.is_valid():
            # This calls Student.save() method for each form entry
            # and does not behave the same as saving a queryset all at once
            formset.save()
            # show success message
            message = "The users have been assigned the role of instructor successfully."
            return render(request, 'database_manager/message.html', {'message': message})
    # if a GET (or any other method) we'll create a blank formset
    else:
        formset = AssignInstructorRoleToUsersFormset(queryset=Instructor.objects.none())

    title = "Assign Instructor role to Users"
    return render(request, 'database_manager/display_formset.html', {'title': title, 'formset': formset})


@login_required
@permission_required('database_manager.view_course', raise_exception=True)
def view_course_attendance_details(request, course_id):
    '''
    View to get attendance details for a course. Additionally, if the user accessing this view
    is neither a superuser nor an admin, he must be an instructor for this course otherwise
    Http 403 (Permission Denied) error is raised.
    '''
    related_course = get_object_or_404(Course, id=course_id)
    if (not request.user.is_superuser) and (not hasattr(request.user, 'admin')):
        num_ins_c = request.user.instructor_for_courses.filter(id=course_id)
        num_ta_c = request.user.teaching_assistant_for_courses.filter(id=course_id)
        if len(num_ins_c) + len(num_ta_c) <= 0:
            raise PermissionDenied
    lectures = ClassEvent.objects.filter(course=related_course, class_type='L')
    tutorials = ClassEvent.objects.filter(course=related_course, class_type='T')
    practicals = ClassEvent.objects.filter(course=related_course, class_type='P')
    context = {'related_course': related_course, 'lectures': lectures,
        'tutorials': tutorials, 'practicals': practicals}
    return render(request, 'database_manager/view_course_attendance_details.html', context)


@login_required
def view_student_attendance_details_in_a_course(request, course_id, student_id):
    '''
    View to get attendance details of a student for a course. Additionally, if the user accessing this
    view is neither a superuser nor an admin nor an instructor or teaching assistant for that course,
    he must be the student for whom the information is being requested otherwise
    Http 403 (Permission Denied) error is raised.
    '''
    related_course = get_object_or_404(Course, id=course_id)
    related_student = get_object_or_404(Student, id=student_id)
    if (not request.user.is_superuser) and (not hasattr(request.user, 'admin')):
        num_ins_c = request.user.instructor_for_courses.filter(id=course_id)
        num_ta_c = request.user.teaching_assistant_for_courses.filter(id=course_id)
        if len(num_ins_c) + len(num_ta_c) <= 0:
            if hasattr(request.user, 'student'):
                if request.user.student.id != student_id:
                    raise PermissionDenied
                elif len(request.user.registered_student_for_courses.filter(id=course_id)) <= 0:
                    raise PermissionDenied
            else:
                raise PermissionDenied
    lectures = ClassEvent.objects.filter(course=related_course, class_type='L')
    tutorials = ClassEvent.objects.filter(course=related_course, class_type='T')
    practicals = ClassEvent.objects.filter(course=related_course, class_type='P')
    context = {'related_course': related_course, 'related_student': related_student,
        'lectures': lectures, 'tutorials': tutorials, 'practicals': practicals}
    return render(request, 'database_manager/view_student_attendance_details_in_a_course.html', context)
