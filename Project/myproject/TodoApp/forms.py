from django import forms
from .models import TodoApp

# ModelForm_________!

class TodoForm(forms.ModelForm):
    class Meta:
        model = TodoApp
        fields = ['t_title', 't_desc', 't_completed']
