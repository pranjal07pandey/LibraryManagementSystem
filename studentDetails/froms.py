from django import forms
from .models import StudentsDetail, BookIssue


class NewStudentForm(forms.ModelForm):
    class Meta:
        model = StudentsDetail
        fields = ('s_id', 'name', 'address', 'contactNo', 'dateOfBirth', 'rollNumber', 'guardianName',
                  'batch', 'grade', 'section', 'gender', 'email')


class BookIssueForm(forms.ModelForm):
    class Meta:
        model = BookIssue
        fields = ('s_id', 'b_id', 'startDate', 'endDate')

