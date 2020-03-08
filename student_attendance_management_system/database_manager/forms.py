from django import forms
from .models import Student


class AddStudentForm(forms.Form):
    entry_number = forms.CharField(max_length=15)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email_address = forms.EmailField()
    def clean_entry_number(self):
        return self.cleaned_data['entry_number'].lower()
