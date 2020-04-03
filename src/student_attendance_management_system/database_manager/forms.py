from django import forms
from django.contrib.auth import get_user_model


class AddStudentForm(forms.Form):
    entry_number = forms.CharField(max_length=15)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email_address = forms.EmailField()
    def clean_entry_number(self):
        return self.cleaned_data['entry_number'].lower()


class AddClassEventCoordinatorForm(forms.Form):
    # Although ClassEventCoordinator has no class_event_coordinator_id field,
    # it will be used for the generalization of the ClassEventCoordinator,
    # i.e. for Instructor, TeachingAssistant, LabAttendant
    class_event_coordinator_id = forms.CharField(max_length=15)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email_address = forms.EmailField()
    def clean_entry_number(self):
        return self.cleaned_data['instructor_id'].lower()


class AddCourseForm(forms.Form):
    entry_number = forms.CharField(max_length=15)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email_address = forms.EmailField()
    def clean_entry_number(self):
        return self.cleaned_data['entry_number'].lower()


class AddClassEventCoordinatorExistingUserForm(forms.Form):
    # show only those choices who are not already Class Event Coordinators, but are existing Users
    user = forms.ModelChoiceField(get_user_model().objects.filter(classeventcoordinator__isnull=True))
    class_event_coordinator_id = forms.CharField(max_length=15)
