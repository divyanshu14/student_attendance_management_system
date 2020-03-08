from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User, Group
from django.forms import formset_factory
from .forms import AddStudentForm
from .models import Student


DEFAULT_PASSWORD = "new_password"


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

    return render(request, 'database_manager/display_formset.html', {'formset': formset, 'num_students': num_students})
