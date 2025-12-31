from django.urls import path
from .views import all_tasks, create_tasks,delete_task,update_tasks

urlpatterns = [
    path("My_tasks/",all_tasks,name="tasks_list"),
    path("create_task/", create_tasks,name="create_task"),
    path("update/<int:pk>/", update_tasks, name="update_tasks"),
    path("delete/<int:pk>/", delete_task, name="delete_task"),
]