from django.db import models
from statuses.models import Status
from labels.models import Label
from django.contrib.auth.models import User


class Task(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True, related_name='author')
    executor = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True,)
    status = models.ForeignKey(Status, on_delete=models.PROTECT, blank=True, null=True)
    labels = models.ManyToManyField(Label, blank=True, related_name='labels', through='TaskLabel')

    def __str__(self):
        return self.name


class TaskLabel(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    label = models.ForeignKey(Label, on_delete=models.RESTRICT)