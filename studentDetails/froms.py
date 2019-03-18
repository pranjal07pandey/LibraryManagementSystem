from django import forms
from .models import StudentsDetail


class NewStudentForm(forms.ModelForm):
    class Meta:
        model = StudentsDetail
        fields = ('s_id', 'name', 'address', 'contactNo', 'dateOfBirth', 'rollNumber', 'guardianName',
                  'batch', 'grade', 'section', 'gender', 'email')
