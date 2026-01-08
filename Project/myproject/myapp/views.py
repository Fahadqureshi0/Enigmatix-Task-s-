from django.shortcuts import render #type:ignore
from django.urls import reverse_lazy#type:ignore
from django.views.generic import ListView, CreateView, UpdateView, DeleteView #type:ignore
from .models import TodoApp

# ListView______!
class TodoListview(ListView):
    model = TodoApp
    template_name = "myapp/list.html"
    context_object_name = 'todo'


# Create View_____!
class TodoCreateView(CreateView):
    model = TodoApp
    fields = ['title', 'desc']
    template_name = 'myapp/create_todo.html'
    success_url = reverse_lazy('todo_list')


# update View______!
class TodoUpdateView(UpdateView):
    model = TodoApp
    fields = ['title', 'desc']
    template_name = 'myapp/update_todo.html'
    success_url = reverse_lazy('todo_list')


# Delete View_____!
class TodoDeleteView(DeleteView):
    model = TodoApp
    template_name = 'myapp/delete_todo.html'
    success_url = reverse_lazy('todo_list')