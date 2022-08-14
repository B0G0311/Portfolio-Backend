from rest_framework import serializers
from .models import Project, Technology


# Remember to move ProjectSerializer under TechnologySerializer
class ProjectSerializer(serializers.ModelSerializer):
    technology = serializers.StringRelatedField(many=True)

    class Meta:
        model = Project
        fields = ["title", "description", "technology", "image"]


class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = '__all__'
