from rest_framework import viewsets, status, parsers, response, decorators
from .models import Job, Position
from .serializers import JobSerializer, PositionSerializer, ResumeUploadSerializer


class PositionViewSet(viewsets.ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer

    @decorators.action(detail=True, methods=['PUT'])
    def move(self, request, pk):
        obj = self.get_object()
        new_order = request.data.get('order')
        Position.objects.move(obj, new_order)
        return response.Response()


class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

    @decorators.action(
        detail=True,
        methods=['PUT'],
        serializer_class=ResumeUploadSerializer,
        parser_classes=[parsers.MultiPartParser]
    )
    def resume_upload(self, request, pk):
        obj = self.get_object()
        serializer = self.serializer_class(
            obj, data=request.data, partial=True, context={"request": request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(serializer.data)

    @decorators.action(detail=True, methods=['PUT'])
    def position_change(self, request, pk):
        obj = self.get_object()
        serializer = self.serializer_class(
            obj, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(serializer.data)
