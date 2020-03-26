from rest_framework import viewsets
from .models import Job, Position
from .serializers import JobSerializer, PositionSerializer
from .serializers import PositionSerializer

Job.objects.all().delete()


class PositionViewSet(viewsets.ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer


class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
