
from django.shortcuts import render, redirect

from .models import FacultyDetails
from .forms import NewFacultyForm

# Create your views here.


#Crud for faculty Starts:

def list_faculty(request):
    faculty = FacultyDetails.objects.all()
    return render(request, 'faculty/list_faculty.html', context={'faculty': faculty})


def add_faculty(request):
        form = NewFacultyForm(request.POST, request.FILES or None)

        if form.is_valid():
            form.save()
            return redirect('list_faculty')

        return render(request, 'faculty/new_faculty.html', {'form': form})


def update_faculty(request, f_id):
    faculty = FacultyDetails.objects.get(f_id=f_id)
    form = NewFacultyForm(request.POST, request.FILES or None, instance=faculty)

    if form.is_valid():
        form.save()
        return redirect('list_faculty')

    return render(request, 'faculty/update_faculty.html', {'form': form, 'faculty':faculty})


def delete_faculty(request, f_id):
    faculty = FacultyDetails.objects.get(f_id=f_id)
    faculty.delete()
    return redirect('list_faculty')

