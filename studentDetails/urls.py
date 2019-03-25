
from django.urls import path
from .import views
# from django.conf.urls import url

urlpatterns = [


    path('list-student/', views.list_students, name='list_students'),
    path('add-student/', views.add_students, name='add_students'),
    path('update-student/<str:s_id>/', views.update_students, name='update_students'),
    path('delete-student/<str:s_id>/', views.delete_students, name='delete_students'),

    path('list-issued-books/', views.list_issued_books, name='list_issued_books'),
    path('book-issue/', views.book_issue, name='book_issue'),
    path('book-return/<int:id>/', views.book_return, name='book_return'),





]
