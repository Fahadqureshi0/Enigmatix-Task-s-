from django.db import models #type:ignore

# TodoApp model:

class TodoApp(models.Model):
    title = models.CharField(max_length=20)
    desc = models.TextField()
    is_completed = models.BooleanField(default=False)


def __str__(self):
    return self.title




