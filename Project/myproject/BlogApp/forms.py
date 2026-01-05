from django import forms
from .models import BlogModel

# BlogForm______!

class BlogForm(forms.ModelForm):
    class Meta:
        model= BlogModel
        fields = ['B_title', 'B_content', 'B_publish', 'B_status']


