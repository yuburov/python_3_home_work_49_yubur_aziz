
from rest_framework import viewsets
from .serializers import TaskSerializer, ProjectSerializer
from webapp.models import Task, Project

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

