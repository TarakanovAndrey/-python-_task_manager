from django.db import models
from statuses.models import Status
from labels.models import Label
from django.contrib.auth.models import User


class Task(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    author_fullname = models.CharField(max_length=150)
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='author_id', blank=True, null=True)
    executor = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True,)
    executor_fullname = models.CharField(max_length=150)
    status = models.ForeignKey(Status, on_delete=models.PROTECT, blank=True, null=True)
    labels = models.ManyToManyField(Label, blank=True)

    def __str__(self):
        return self.name
