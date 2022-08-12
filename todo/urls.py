from django.urls import path
from . import views

urlpatterns = [
    path('todo/', views.todo_list),
    path('todo/<int:todo_id>/', views.todo_detail),
    path('todo/mark_complete/<int:todo_id>', views.mark_complete),
]
