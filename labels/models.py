from django.db import models


class Label(models.Model):
    label_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.label_name
