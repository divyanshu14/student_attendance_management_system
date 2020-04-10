from django import forms
from django.contrib.auth import get_user_model
from .models import ClassEventCoordinator


class AddStudentForm(forms.Form):
    entry_number = forms.CharField(max_length=15)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=150)
    email_address = forms.EmailField()


class AddStudentExistingUserForm(forms.Form):
    user = forms.ModelChoiceField(get_user_model().objects.filter(student__isnull=True))
    entry_number = forms.CharField(max_length=15)


class AddInstructorForm(forms.Form):
    instructor_id = forms.CharField(max_length=15)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=150)
    email_address = forms.EmailField()


class AddInstructorExistingUserForm(forms.Form):
    instructor_id = forms.CharField(max_length=15)
    user = forms.ModelChoiceField(get_user_model().objects.filter(classeventcoordinator__isnull=True))


class AddInstructorExistingClassEventCoordinatorForm(forms.Form):
    instructor_id = forms.CharField(max_length=15)
    class_event_coordinator = forms.ModelChoiceField(ClassEventCoordinator.objects.filter(instructor__isnull=True))


class AddTeachingAssistantForm(forms.Form):
    teaching_assistant_id = forms.CharField(max_length=15)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=150)
    email_address = forms.EmailField()


class AddTeachingAssistantExistingUserForm(forms.Form):
    teaching_assistant_id = forms.CharField(max_length=15)
    user = forms.ModelChoiceField(get_user_model().objects.filter(classeventcoordinator__isnull=True))


class AddTeachingAssistantExistingClassEventCoordinatorForm(forms.Form):
    teaching_assistant_id = forms.CharField(max_length=15)
    class_event_coordinator = forms.ModelChoiceField(ClassEventCoordinator.objects.filter(teachingassistant__isnull=True))


# class AddLabAttendantForm(forms.Form):
#     lab_attendant_id = forms.CharField(max_length=15)
#     first_name = forms.CharField(max_length=30)
#     last_name = forms.CharField(max_length=150)
#     email_address = forms.EmailField()


# class AddLabAttendantExistingUserForm(forms.Form):
#     lab_attendant_id = forms.CharField(max_length=15)
#     user = forms.ModelChoiceField(get_user_model().objects.filter(classeventcoordinator__isnull=True))


# class AddLabAttendantExistingClassEventCoordinatorForm(forms.Form):
#     lab_attendant_id = forms.CharField(max_length=15)
#     class_event_coordinator = forms.ModelChoiceField(ClassEventCoordinator.objects.filter(labattendant__isnull=True))
