from django import forms


class NumStudentsToAddForm(forms.Form):
    num_students_to_add = forms.IntegerField(min_value=1)


class NumInstructorsToAddForm(forms.Form):
    num_instructors_to_add = forms.IntegerField(min_value=1)


class NumCoursesToAddForm(forms.Form):
    num_courses_to_add = forms.IntegerField(min_value=1)
