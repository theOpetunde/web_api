from rest_framework import serializers
from . import models

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Project
        fields = ('id', 'name', 'description', 'completed')


class ActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Action
        fields = ('id', 'project_id', 'description', 'notes', 'completed')
        
