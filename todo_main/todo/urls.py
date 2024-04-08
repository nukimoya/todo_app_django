from django.urls import path
from . import views

urlpatterns = [
    path('addTask/', views.addtask, name = 'addtask'),
    path('mark_done/<int:pk>/', views.mark_done, name = 'mark_done'),
    path('mark_undone/<int:pk>/', views.mark_undone, name = 'mark_undone'),
    path('removeTask/<int:pk>/', views.removetask, name = 'removetask'),
    path('editTask/<int:pk>/', views.edittask, name = 'edittask'),
]