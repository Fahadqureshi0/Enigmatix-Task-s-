from django.db import models

# To-Do Model______!

class TodoApp(models.Model):
    t_title = models.CharField(max_length=100)
    t_desc = models.TextField()
    t_completed = models.BooleanField(default=False)
    t_created_at = models.DateTimeField(auto_now_add=True)
    t_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.t_title   