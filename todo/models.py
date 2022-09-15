from django.db import models
from django.contrib.auth.models import User

# import uuid
import uuid


class Task(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    # description = models.TextField()
    completed = models.BooleanField(default=False, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, related_name='tasks', on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.title

