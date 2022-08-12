from rest_framework import serializers
from . models import Todo

class TodoSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    completed = serializers.ReadOnlyField()
    created_at = serializers.ReadOnlyField()
    
    class Meta:
        model = Todo
        fields = ['id', 'title', 'body', 'date', 'time', 'completed', 'created_at']


class TodoListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Todo
        fields = ['id', 'title']

    