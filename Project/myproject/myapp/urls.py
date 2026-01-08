from django.urls import path #type:ignore
from .views import TodoCreateView, TodoDeleteView, TodoListview, TodoUpdateView


urlpatterns = [
    path('', TodoListview.as_view(), name='todo_list'),
    path('add_tasks/', TodoCreateView.as_view(), name="create_task"),
    path('update/<int:pk>/', TodoUpdateView.as_view(), name='update_task'),
    path('delete/<int:pk>/', TodoDeleteView.as_view(), name='delete_task'),
]