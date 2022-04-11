from django.urls import path
from . import views

urlpatterns = [
    path('', views.todoappView, name='home'),
    path('addTodoItem/', views.addTodoView, name='add_item'),
    path('deleteTodoItem/<int:pk>/', views.deleteTodoView, name='delete_item')
]