from rest_framework import serializers
from .models import Project, Technology


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ["title", "description", "technology", "user"]
        # Add images after technology and fix


class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = ["technology"]
