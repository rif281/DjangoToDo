from django.db import models


class Task(models.Model):
    task_title = models.CharField(max_length=200)
    task_description = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task_title


