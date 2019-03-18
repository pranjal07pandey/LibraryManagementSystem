from django import forms
from .models import FacultyDetails


class NewFacultyForm(forms.ModelForm):
    class Meta:
        model = FacultyDetails
        fields = ('f_id', 'name', 'contact', 'address', 'email', 'designation', 'subject')

