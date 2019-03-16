from django.shortcuts import render,redirect

from .models import BookDetail
from .forms import NewBookForm
# Create your views here.


def index(request):
    return render(request,'index.html')


def list_books(request):
    books = BookDetail.objects.all()
    return render(request, 'books/list_books.html', context={'books': books})


def add_books(request):
        form = NewBookForm(request.POST, request.FILES or None)

        if form.is_valid():
            form.save()
            return redirect('list_books')

        return render(request, 'books/new_books.html', {'form': form})


def update_books(request, b_id):
    books = BookDetail.objects.get(b_id=b_id)
    form = NewBookForm(request.POST, request.FILES or None, instance=books)

    if form.is_valid():
        form.save()
        return redirect('list_books')

    return render(request, 'books/update_books.html', {'form': form, 'books':books})


def delete_books(request, b_id):
    books = BookDetail.objects.get(b_id=b_id)
    books.delete()
    return redirect('list_books')

















