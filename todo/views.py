from rest_framework import generics, viewsets
from todo.serializers import UserSerializer, TaskSerializer
from todo.models import User, Task
from django.db.models import Q

class User(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class TaskList(generics.ListCreateAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        queryset = Task.objects.all()
        status = self.request.query_params.get('status', None)
        username = self.request.query_params.get('username', None)
        aQ = Q()
        if status is not None:
            aQ.add(Q(status=status), Q.AND)
        if username is not None:
            aQ.add(Q(username=username), Q.AND)
        queryset = queryset.filter(aQ)
        return queryset

class TaskUpdateViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


class TaskAdd(generics.CreateAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

