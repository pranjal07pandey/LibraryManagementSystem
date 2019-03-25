from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import BookDetail
from .forms import NewBookForm
from django.contrib import messages
# Create your views here.


@login_required(login_url='login')
def index(request):
    return render(request,'index.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account Created for {username}!')
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('login')


# Crud for Books Starts:
@login_required(login_url='login')
def list_books(request):
    books = BookDetail.objects.all()
    return render(request, 'books/list_books.html', context={'books': books})


@login_required(login_url='login')
def add_books(request):
        form = NewBookForm(request.POST, request.FILES or None)

        if form.is_valid():
            form.save()
            return redirect('list_books')

        return render(request, 'books/new_books.html', {'form': form})


@login_required(login_url='login')
def update_books(request, b_id):
    books = BookDetail.objects.get(b_id=b_id)
    form = NewBookForm(request.POST, request.FILES or None, instance=books)

    if form.is_valid():
        form.save()
        return redirect('list_books')

    return render(request, 'books/update_books.html', {'form': form, 'books':books})


@login_required(login_url='login')
def delete_books(request, b_id):
    books = BookDetail.objects.get(b_id=b_id)
    books.delete()
    return redirect('list_books')

# Crud for books ends











