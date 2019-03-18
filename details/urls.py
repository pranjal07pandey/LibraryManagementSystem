"""LibraryManagementSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from .import views
# from django.conf.urls import url

urlpatterns = [

    path('', views.index, name='index'),

    path('list-book/', views.list_books, name='list_books'),
    path('add-book/', views.add_books, name='add_books'),
    path('update-book/<str:b_id>/', views.update_books, name='update_books'),
    path('delete-book/<str:b_id>/', views.delete_books, name='delete_books'),


]
