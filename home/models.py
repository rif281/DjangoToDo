from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    task_title = models.CharField(max_length=200)
    task_description = models.TextField()
    status = models.BooleanField(default=False)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task_title


