from django.db import models


class Status(models.Model):
    status_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.status_name
