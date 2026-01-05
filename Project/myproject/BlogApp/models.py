from django.db import models
from django.contrib.auth.models import User 
from django.utils import timezone

# Status Model_________!
class BlogModel(models.Model):

    STATUS_CHOICES = [
        ('DF', 'Draft'),
        ('PB', 'Published'),
    ]

    B_author = models.ForeignKey(User, on_delete=models.CASCADE)
    B_title = models.CharField(max_length=20)
    B_slug = models.SlugField(max_length=30, unique_for_date='B_publish')
    B_content = models.TextField(blank=True)
    B_publish = models.DateTimeField(default=timezone.now)
    B_created = models.DateTimeField(auto_now_add=True)
    B_updated = models.DateTimeField(auto_now=True)
    B_status = models.CharField(max_length=2,choices=STATUS_CHOICES,default='DF'
    )

    def __str__(self):
        return self.B_title



