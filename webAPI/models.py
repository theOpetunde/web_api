from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=255, required=True)
    description = models.TextField(required=True)
    completed = models.BooleanField()


class Action(models.Model):
    project_id = models.ForeignKey(Project, On_delete=models.CASCADE)
    description = models.CharField(max_length = 128, required=True)
    notes = models.TextField(required=True)
    completed = models.BooleanField()