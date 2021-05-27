from django.urls import path
from . import  views

urlpatterns = [
    path('', views.upload, name="upload"),
    path('showdata/', views.showdata, name="showdata"),
    path('update_data/', views.update_data, name="update_data"),
    path('delete_data/', views.delete_data, name="delete_data"),
    path('add_data/', views.add_data, name="add_data"),
]