from django.shortcuts import render, redirect

from .models import StudentsDetail
from .froms import NewStudentForm

# Create your views here.



#Crud for Students Starts:


def list_students(request):
    students = StudentsDetail.objects.all()
    return render(request, 'students/list_students.html', context={'students': students})


def add_students(request):
        form = NewStudentForm(request.POST, request.FILES or None)

        if form.is_valid():
            form.save()
            return redirect('list_students')

        return render(request, 'students/new_students.html', {'form': form})


def update_students(request, s_id):
    students = StudentsDetail.objects.get(s_id=s_id)
    form = NewStudentForm(request.POST, request.FILES or None, instance=students)

    if form.is_valid():
        form.save()
        return redirect('list_students')

    return render(request, 'students/update_students.html', {'form': form, 'students':students})


def delete_students(request, s_id):
    students = StudentsDetail.objects.get(s_id=s_id)
    students.delete()
    return redirect('list_students')

# Crud for students ends