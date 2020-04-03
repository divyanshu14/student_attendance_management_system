from django import forms


class AddStudentForm(forms.Form):
    entry_number = forms.CharField(max_length=15)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email_address = forms.EmailField()
    def clean_entry_number(self):
        return self.cleaned_data['entry_number'].lower()


class AddInstructorForm(forms.Form):
    instructor_id = forms.CharField(max_length=15)
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
