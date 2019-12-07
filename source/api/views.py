
from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly

from .serializers import TaskSerializer, ProjectSerializer
from webapp.models import Task, Project

class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

class ProjectViewSet(viewsets.ModelViewSet):
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

