from todo.models import User, Task
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'username', 'description', 'status', 'start', 'expire', 'down', 'priority')
        lookup_field = 'id'


