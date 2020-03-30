from rest_framework import viewsets, status, parsers, response, decorators
from .models import Job, Position
from .serializers import JobSerializer, PositionSerializer, JobResumeSerializer


class PositionViewSet(viewsets.ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer


class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

    @decorators.action(
        detail=True,
        methods=['PUT'],
        serializer_class=JobResumeSerializer,
        parser_classes=[parsers.MultiPartParser]
    )
    def resume_upload(self, request, pk):
        obj = self.get_object()
        serializer = self.serializer_class(
            obj, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(serializer.data)
