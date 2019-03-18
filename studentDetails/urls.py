
from django.urls import path
from .import views
# from django.conf.urls import url

urlpatterns = [


    path('list-student/', views.list_students, name='list_students'),
    path('add-student/', views.add_students, name='add_students'),
    path('update-student/<str:s_id>/', views.update_students, name='update_students'),
    path('delete-student/<str:s_id>/', views.delete_students, name='delete_students'),




]
