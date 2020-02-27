from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=255, required=True)
    description = models.TextField(required=True)
    completed = models.BooleanField()