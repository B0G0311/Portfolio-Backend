from django.db import models
from django.contrib.auth.models import User


class Technology(models.Model):
    technology = models.CharField(max_length=20)

    def __str__(self):
        return self.technology


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.ManyToManyField('Technology', related_name='project_api')
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title
