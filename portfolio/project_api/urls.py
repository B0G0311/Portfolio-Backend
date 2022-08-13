from django.urls import path
from .views import (
    ProjectListApiView,
    ProjectDetailApiView,
    TechnologyView,
)


urlpatterns = [
    path('api/', ProjectListApiView.as_view()),
    path('api/<int:project_id>/', ProjectDetailApiView.as_view()),
    path('<technology>/', TechnologyView.as_view()),
]
