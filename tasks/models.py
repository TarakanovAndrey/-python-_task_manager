from django.db import models
from statuses.models import Status
from labels.models import Label
from django.contrib.auth.models import User


class Task(models.Model):
    task_name = models.CharField(max_length=100)
    description = models.TextField(max_length=399)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=150)
    executor = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    labels = models.ManyToManyField(Label)

    def __str__(self):
        return self.task_name
