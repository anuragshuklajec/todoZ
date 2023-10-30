from django.db import models
from django.utils import timezone

# Create your models here.
class Client(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=15)
    email = models.EmailField()

class Todo(models.Model):
    todoType = models.CharField(max_length=25)
    todoBody = models.CharField(max_length=50)
    priorityType = models.CharField(max_length=1)
    isComplete = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.updatedAt = timezone.now()
        super().save(*args, **kwargs)
