from django.db import models

# Create your models here.
class Project(models.Model):
    """Creates a model for the projects in the database"""
    name = models.CharField(max_length=255, required=True)
    description = models.TextField(required=True)
    completed = models.BooleanField()

    def __str__(self):
        """Returns the name of the project"""
        return self.name


class Action(models.Model):
    """Creates a model for the actions created related to specific projects"""
    project_id = models.ForeignKey(Project, On_delete=models.CASCADE)
    description = models.CharField(max_length = 128, required=True)
    notes = models.TextField(required=True)
    completed = models.BooleanField()