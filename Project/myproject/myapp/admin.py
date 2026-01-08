from django.contrib import admin #type:ignore
from .models import TodoApp


admin.site.register(TodoApp)