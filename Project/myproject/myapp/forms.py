from django import forms  #type:ignore
from .models import TodoApp


# To do Form_________!

class TodoForm(forms.ModelForm):
    class Meta:
        model = TodoApp
        fields = ['title', 'desc']


