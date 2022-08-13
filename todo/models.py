from django.db import models
from django.utils import timezone


class Todo(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateField(default=timezone.now)
    time = models.TimeField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    