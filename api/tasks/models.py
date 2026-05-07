from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True) #add* sets time only once
    updated_at = models.DateTimeField(auto_now=True) #continuously updates

    def __str__(self):
        return self.title