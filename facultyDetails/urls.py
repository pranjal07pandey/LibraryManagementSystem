
from django.urls import path
from .import views
# from django.conf.urls import url

urlpatterns = [


    path('list-faculty/', views.list_faculty, name='list_faculty'),
    path('add-faculty/', views.add_faculty, name='add_faculty'),
    path('update-faculty/<str:f_id>/', views.update_faculty, name='update_faculty'),
    path('delete-faculty/<str:f_id>/', views.delete_faculty, name='delete_faculty'),


]