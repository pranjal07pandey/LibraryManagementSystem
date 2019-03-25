from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import datetime
from .models import StudentsDetail, BookIssue
from .froms import NewStudentForm , BookIssueForm


# Create your views here.
# Crud for Students Starts:

@login_required(login_url='login')
def list_students(request):
    students = StudentsDetail.objects.all()
    return render(request, 'students/list_students.html', context={'students': students})


@login_required(login_url='login')
def add_students(request):
    form = NewStudentForm(request.POST, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('list_students')

    return render(request, 'students/new_students.html', {'form': form})


@login_required(login_url='login')
def update_students(request, s_id):
    students = StudentsDetail.objects.get(s_id=s_id)
    form = NewStudentForm(request.POST, request.FILES or None, instance=students)

    if form.is_valid():
        form.save()
        return redirect('list_students')

    return render(request, 'students/update_students.html', {'form': form, 'students': students})


@login_required(login_url='login')
def delete_students(request, s_id):
    students = StudentsDetail.objects.get(s_id=s_id)
    students.delete()
    return redirect('list_students')


# Crud for students ends


@login_required(login_url='login')
def list_issued_books(request):
    issued = BookIssue.objects.all()
    return render(request, 'books/list_issuedBooks.html', context={'issued': issued})


@login_required(login_url='login')
def book_issue(request):
    form = BookIssueForm(request.POST, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('list_issued_books')

    return render(request, 'books/book_issue.html', {'form': form})


def book_return(request, id):
    book = BookIssue.objects.get(id = id)
    form = BookIssueForm(request.POST, request.FILES or None, instance=book)

    if form.is_valid():


        form.save()
        ed = form.cleaned_data['endDate'].today()
        # ed.datetime.date.today()
        issued = BookIssue.objects.all()
        return render(request, 'books/list_issuedBooks.html', context={'issued': issued, 'ed':ed})

        # return redirect('list_issued_books')
    return render(request, 'books/book_return.html',{'form':form, 'book':book})











