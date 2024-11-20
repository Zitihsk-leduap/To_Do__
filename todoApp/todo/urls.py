from django.urls import path,include
from . import views


urlpatterns = [
    path('', views.main, name='main'),
    path('todo/<int:todo_id>/delete/', views.todo_delete, name="todo_delete"),
    path('todo/<int:todo_id>/edit/', views.todo_edit, name="todo_edit"),  # Correct name here
]
