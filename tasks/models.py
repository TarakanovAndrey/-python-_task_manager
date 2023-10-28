from django.db import models
from statuses.models import Status
from labels.models import Label
from django.contrib.auth.models import User


class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=399, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=150)
    executor = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True,)
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    labels = models.ManyToManyField(Label, blank=True)

    def __str__(self):
        return self.name
