from rest_framework import serializers
from webapp.models import Task, Project

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'summary', 'description', 'status', 'type', 'date_create',
                  'created_by', 'assigned_to', 'project')


class TaskProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'summary', 'description', 'status', 'type', 'date_create',
                  'created_by', 'assigned_to')

class ProjectSerializer(serializers.ModelSerializer):
    tasks = TaskProjectSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ('id', 'name', 'description', 'create_date', 'update_date', 'users', 'tasks')

