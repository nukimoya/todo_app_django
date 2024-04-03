from django.urls import path
from . import views

urlpatterns = [
    path('addTask/', views.addtask, name = 'addtask'),
]