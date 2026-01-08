from django.shortcuts import render, redirect, get_object_or_404 
from .models import TodoApp
from .forms import TodoForm

# To-Do App Views______!
# CRUD Operations______!

# # All Task List_______!
def all_tasks(request):
    tasks = TodoApp.objects.all()
    return render(request, "TodoApp/tasks_list.html", {"tasks":tasks})

# Creating Tasks______!
def  create_tasks(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("tasks_list")
        return render(request, "TodoApp/tasks_form.html", {"form":form})
    else:
            form = TodoForm()
            return render(request, "TodoApp/tasks_form.html", {"form":form})


# Update Tasks______!

def update_tasks(request,pk):
    task = get_object_or_404(TodoApp, id=pk)
    if request.method=="POST":
        form = TodoForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("tasks_list")
        return render(request, "Todo/update_form.html", {"form":form})
    else:
            form = TodoForm(instance=task)
            return render(request, "TodoApp/update_form.html", {"form":form})

# Delete_task________!

def delete_task(request, pk):
    task = get_object_or_404(TodoApp, id=pk)
    if request.method == "POST":
        task.delete()
        return redirect("tasks_list")
    return render(request, "TodoApp/task_delete.html", {"task":task})



