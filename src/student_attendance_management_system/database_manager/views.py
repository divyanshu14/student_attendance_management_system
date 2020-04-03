from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Group
from django.forms import formset_factory, modelformset_factory
from database_manager.forms import (
    AddStudentForm, AddStudentExistingUserForm, AddInstructorForm,
    AddInstructorExistingUserForm, AddInstructorExistingClassEventCoordinatorForm,
    AddTeachingAssistantForm, AddTeachingAssistantExistingUserForm,
    AddTeachingAssistantExistingClassEventCoordinatorForm
)
from database_manager.models import (
    Student, ClassEventCoordinator, Instructor, TeachingAssistant, Course, ClassEvent
)
from django.core.exceptions import PermissionDenied
from django.contrib.auth import get_user_model


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


# def is_lab_attendant(user):
#     '''
#     Returns True if the user belongs to Lab Attendant group, otherwise returns False.
#     '''
#     return user.groups.filter(name='Lab Attendants').exists()


@login_required
@permission_required('database_manager.add_student', raise_exception=True)
def add_students(request, num_students):
    '''
    View to add students.
    '''
    AddStudentFormSet = formset_factory(AddStudentForm, extra=num_students)
    # if this is a POST request we need to process the formset data
    if request.method == 'POST':
        # create a formset instance and populate it with data from the request:
        formset = AddStudentFormSet(request.POST)
        # check whether it's valid:
        if formset.is_valid():
            # process the data in formset.cleaned_data as required
            for form in formset:
                user = get_user_model().objects.create_user(form.cleaned_data['email_address'],
                                                            DEFAULT_PASSWORD
                                                            )
                user.first_name = form.cleaned_data['first_name']
                user.last_name = form.cleaned_data['last_name']
                user.save()
                Student.objects.create(
                    user=user, entry_number=form.cleaned_data['entry_number'])
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
                user = get_user_model().objects.create_user(form.cleaned_data['email_address'],
                                                            DEFAULT_PASSWORD
                                                            )
                user.first_name = form.cleaned_data['first_name']
                user.last_name = form.cleaned_data['last_name']
                user.save()
                class_event_coordinator = ClassEventCoordinator.objects.create(
                    user=user)
                Instructor.objects.create(class_event_coordinator=class_event_coordinator,
                                          instructor_id=form.cleaned_data['instructor_id']
                                          )
            # show success message
            message = "The instructors' data has been saved successfully."
            return render(request, 'database_manager/message.html', {'message': message})
    # if a GET (or any other method) we'll create a blank formset
    else:
        formset = AddInstructorFormSet()

    title = "Add Instructors"
    return render(request, 'database_manager/display_formset.html', {'title': title, 'formset': formset})


@login_required
@permission_required('database_manager.add_teaching_assistant', raise_exception=True)
def add_teaching_assistants(request, num_teaching_assistants):
    '''
    View to add teaching assistants.
    '''
    AddTeachingAssistantFormSet = formset_factory(AddTeachingAssistantForm,
                                                  extra=num_teaching_assistants
                                                  )
    # if this is a POST request we need to process the formset data
    if request.method == 'POST':
        # create a formset instance and populate it with data from the request:
        formset = AddTeachingAssistantFormSet(request.POST)
        # check whether it's valid:
        if formset.is_valid():
            # process the data in formset.cleaned_data as required
            for form in formset:
                user = get_user_model().objects.create_user(form.cleaned_data['email_address'],
                                                            DEFAULT_PASSWORD
                                                            )
                user.first_name = form.cleaned_data['first_name']
                user.last_name = form.cleaned_data['last_name']
                user.save()
                class_event_coordinator = ClassEventCoordinator.objects.create(
                    user=user)
                TeachingAssistant.objects.create(user=user,
                                                 teaching_assistant_id=form.cleaned_data['teaching_assistant_id']
                                                 )
            # show success message
            message = "The teaching assistants' data has been saved successfully."
            return render(request, 'database_manager/message.html', {'message': message})
    # if a GET (or any other method) we'll create a blank formset
    else:
        formset = AddTeachingAssistantFormSet()

    title = "Add Teaching Assistants"
    return render(request, 'database_manager/display_formset.html', {'title': title, 'formset': formset})


# @login_required
# @permission_required('database_manager.add_lab_attendant', raise_exception=True)
# def add_lab_attendants(request, num_lab_attendants):
#     '''
#     View to add lab attendants.
#     '''
#     AddLabAttendantFormSet = formset_factory(AddLabAttendantForm,
#         extra=num_lab_attendants
#     )
#     # if this is a POST request we need to process the formset data
#     if request.method == 'POST':
#         # create a formset instance and populate it with data from the request:
#         formset = AddLabAttendantFormSet(request.POST)
#         # check whether it's valid:
#         if formset.is_valid():
#             # process the data in formset.cleaned_data as required
#             for form in formset:
#                 user = get_user_model().objects.create_user(form.cleaned_data['email_address'],
#                     DEFAULT_PASSWORD
#                 )
#                 user.first_name = form.cleaned_data['first_name']
#                 user.last_name = form.cleaned_data['last_name']
#                 user.save()
#                 class_event_coordinator = ClassEventCoordinator.objects.create(user=user)
#                 LabAttendant.objects.create(user=user,
#                     lab_attendant_id=form.cleaned_data['lab_attendant_id']
#                 )
#             # show success message
#             message = "The lab attendants' data has been saved successfully."
#             return render(request, 'database_manager/message.html', {'message': message})
#     # if a GET (or any other method) we'll create a blank formset
#     else:
#         formset = AddLabAttendantFormSet()

#     title = "Add Lab Attendants"
#     return render(request, 'database_manager/display_formset.html', {'title': title, 'formset': formset})


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
    Useful in cases when someone joined the institute as an admin or instructor or teaching assistant
    (and has already been registered), but later got enrolled in some course in the institute.
    '''
    AddStudentExistingUserFormSet = formset_factory(
        AddStudentExistingUserForm, extra=num_users)
    # if this is a POST request we need to process the formset data
    if request.method == 'POST':
        # create a formset instance and populate it with data from the request:
        formset = AddStudentExistingUserFormSet(request.POST)
        # check whether it's valid:
        if formset.is_valid():
            for form in formset:
                Student.objects.create(user=form.cleaned_data['user'],
                                       entry_number=form.cleaned_data['entry_number']
                                       )
            # show success message
            message = "The users have been assigned the role of student successfully."
            return render(request, 'database_manager/message.html', {'message': message})
    # if a GET (or any other method) we'll create a blank formset
    else:
        formset = AddStudentExistingUserFormSet(
            queryset=Student.objects.none())

    title = "Assign Student role to Users"
    return render(request, 'database_manager/display_formset.html', {'title': title, 'formset': formset})


@login_required
@permission_required('database_manager.add_instructor', raise_exception=True)
def assign_instructor_role_to_users(request, num_users):
    '''
    View to assign instructor role to users.
    Useful in cases when someone joined the institute as a student or admin
    (and has already been registered), but later became an instructor in the institute.
    '''
    AddInstructorExistingUserFormSet = formset_factory(AddInstructorExistingUserForm,
                                                       extra=num_users
                                                       )
    # if this is a POST request we need to process the formset data
    if request.method == 'POST':
        # create a formset instance and populate it with data from the request:
        formset = AddInstructorExistingUserFormSet(request.POST)
        # check whether it's valid:
        if formset.is_valid():
            for form in formset:
                user = form.cleaned_data['user']
                class_event_coordinator = ClassEventCoordinator.objects.create(
                    user=user)
                Instructor.objects.create(class_event_coordinator=class_event_coordinator,
                                          instructor_id=form.cleaned_data['instructor_id']
                                          )
            # show success message
            message = "The users have been assigned the role of instructor successfully."
            return render(request, 'database_manager/message.html', {'message': message})
    # if a GET (or any other method) we'll create a blank formset
    else:
        formset = AddInstructorExistingUserFormSet()

    title = "Assign Instructor role to Users"
    return render(request, 'database_manager/display_formset.html', {'title': title, 'formset': formset})


@login_required
@permission_required('database_manager.add_instructor', raise_exception=True)
def assign_instructor_role_to_class_event_coordinator(request, num_class_event_coordinators):
    '''
    View to assign instructor role to class event coordinators.
    Useful in cases when someone joined the institute as a teaching assistant
    (and has already been registered), but later became an instructor in the institute.
    '''
    AddInstructorExistingClassEventCoordinatorFormSet = formset_factory(
        AddInstructorExistingClassEventCoordinatorForm,
        extra=num_class_event_coordinators
    )
    # if this is a POST request we need to process the formset data
    if request.method == 'POST':
        # create a formset instance and populate it with data from the request:
        formset = AddInstructorExistingClassEventCoordinatorFormSet(
            request.POST)
        # check whether it's valid:
        if formset.is_valid():
            for form in formset:
                Instructor.objects.create(
                    class_event_coordinator=form.cleaned_data['class_event_coordinator'],
                    instructor_id=form.cleaned_data['instructor_id']
                )
            # show success message
            message = "The class event coordinators have been assigned the role of instructor successfully."
            return render(request, 'database_manager/message.html', {'message': message})
    # if a GET (or any other method) we'll create a blank formset
    else:
        formset = AddInstructorExistingClassEventCoordinatorFormSet(
            queryset=Instructor.objects.none())

    title = "Assign Instructor role to Class Event Coordinators"
    return render(request, 'database_manager/display_formset.html', {'title': title, 'formset': formset})


@login_required
@permission_required('database_manager.add_teaching_assistant', raise_exception=True)
def assign_teaching_assistant_role_to_users(request, num_users):
    '''
    View to assign teaching assistant role to users.
    Useful in cases when someone joined the institute as a student or admin
    (and has already been registered), but later became an teaching assistant in the institute.
    '''
    AddTeachingAssistantExistingUserFormSet = formset_factory(AddTeachingAssistantExistingUserForm,
                                                              extra=num_users
                                                              )
    # if this is a POST request we need to process the formset data
    if request.method == 'POST':
        # create a formset instance and populate it with data from the request:
        formset = AddTeachingAssistantExistingUserFormSet(request.POST)
        # check whether it's valid:
        if formset.is_valid():
            for form in formset:
                user = form.cleaned_data['user']
                class_event_coordinator = ClassEventCoordinator.objects.create(
                    user=user)
                TeachingAssistant.objects.create(class_event_coordinator=class_event_coordinator,
                                                 teaching_assistant_id=form.cleaned_data['teaching_assistant_id']
                                                 )
            # show success message
            message = "The users have been assigned the role of teaching assistant successfully."
            return render(request, 'database_manager/message.html', {'message': message})
    # if a GET (or any other method) we'll create a blank formset
    else:
        formset = AddTeachingAssistantExistingUserFormSet()

    title = "Assign Teaching Assistant role to Users"
    return render(request, 'database_manager/display_formset.html', {'title': title, 'formset': formset})


@login_required
@permission_required('database_manager.add_teaching_assistant', raise_exception=True)
def assign_teaching_assistant_role_to_class_event_coordinator(request, num_class_event_coordinators):
    '''
    View to assign teaching assistant role to class event coordinators.
    Useful in cases when someone joined the institute as an instructor
    (and has already been registered), but later became a teaching assistant in the institute.
    '''
    AddTeachingAssistantExistingClassEventCoordinatorFormSet = formset_factory(
        AddTeachingAssistantExistingClassEventCoordinatorForm,
        extra=num_class_event_coordinators, fields=(
            'class_event_coordinator', 'teaching_assistant_id')
    )
    # if this is a POST request we need to process the formset data
    if request.method == 'POST':
        # create a formset instance and populate it with data from the request:
        formset = AddTeachingAssistantExistingClassEventCoordinatorFormSet(
            request.POST)
        # check whether it's valid:
        if formset.is_valid():
            for form in formset:
                TeachingAssistant.objects.create(
                    class_event_coordinator=form.cleaned_data['class_event_coordinator'],
                    teaching_assistant_id=form.cleaned_data['teaching_assistant_id']
                )
            # show success message
            message = "The class event coordinators have been assigned the role of taching assistant successfully."
            return render(request, 'database_manager/message.html', {'message': message})
    # if a GET (or any other method) we'll create a blank formset
    else:
        formset = AddTeachingAssistantExistingClassEventCoordinatorFormSet(
            queryset=TeachingAssistant.objects.none())

    title = "Assign Teaching Assistant role to Class Event Coordinators"
    return render(request, 'database_manager/display_formset.html', {'title': title, 'formset': formset})


@login_required
@permission_required('database_manager.view_course', raise_exception=True)
def view_course_attendance_details(request, course_id):
    '''
    View to get attendance details for a course. Additionally, if the user accessing this view
    is neither a superuser nor an admin, he must be an instructor or teaching assistant for this course
    having database_manager.view_course permission otherwise
    Http 403 (Permission Denied) error is raised.
    '''
    related_course = get_object_or_404(Course, id=course_id)
    if (not request.user.is_superuser) and (not hasattr(request.user, 'admin')):
        num_ins_c = request.user.classeventcoordinator.instructor.course.filter(
            id=course_id)
        num_ta_c = request.user.classeventcoordinator.teaching_assistant.course.filter(
            id=course_id)
        # num_la_c = request.user.classeventcoordinator.lab_attendant.course.filter(id=course_id)
        if len(num_ins_c) + len(num_ta_c) <= 0:
            raise PermissionDenied
    lectures = ClassEvent.objects.filter(course=related_course, class_type='L')
    tutorials = ClassEvent.objects.filter(
        course=related_course, class_type='T')
    practicals = ClassEvent.objects.filter(
        course=related_course, class_type='P')
    context = {'related_course': related_course, 'lectures': lectures,
               'tutorials': tutorials, 'practicals': practicals}
    return render(request, 'database_manager/view_course_attendance_details.html', context)


@login_required
@permission_required('database_manager.view_course', raise_exception=True)
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
        num_ins_c = request.user.classeventcoordinator.instructor.course.filter(
            id=course_id)
        num_ta_c = request.user.classeventcoordinator.teaching_assistant.course.filter(
            id=course_id)
        # num_la_c = request.user.classeventcoordinator.lab_attendant.course.filter(id=course_id)
        if len(num_ins_c) + len(num_ta_c) <= 0:
            if hasattr(request.user, 'student'):
                if request.user.student.id != student_id:
                    raise PermissionDenied
                elif len(request.user.student.course.filter(id=course_id)) <= 0:
                    raise PermissionDenied
            else:
                raise PermissionDenied
    lectures = ClassEvent.objects.filter(course=related_course, class_type='L')
    tutorials = ClassEvent.objects.filter(
        course=related_course, class_type='T')
    practicals = ClassEvent.objects.filter(
        course=related_course, class_type='P')
    context = {'related_course': related_course, 'related_student': related_student,
               'lectures': lectures, 'tutorials': tutorials, 'practicals': practicals}
    return render(request, 'database_manager/view_student_attendance_details_in_a_course.html', context)
