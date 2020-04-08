from rest_framework import viewsets, status, parsers, response, decorators
from .models import Job, Position
from .serializers import JobSerializer, PositionSerializer, ResumeUploadSerializer
from django_filters.rest_framework import DjangoFilterBackend
import yake


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
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['url']

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

    @decorators.action(detail=False, methods=['POST'])
    def keyword_extract(self, request):
        kw_extractor = yake.KeywordExtractor(top=50)
        keywords = kw_extractor.extract_keywords(request.data.get('text'))
        print(keywords)
        return response.Response([keyword[0] for keyword in keywords])
