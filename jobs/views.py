from rest_framework import viewsets, parsers, response, decorators
from .models import Job, Position
from .serializers import JobSerializer, ResumeUploadSerializer
from django_filters.rest_framework import DjangoFilterBackend
from utils.emsi import extract


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
        # print(extract_text(request.data.get('resume')))
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
        data = extract(request.data.get('text'))
        keywords = map(lambda x: x['surfaceForm']['value'], data['trace'])
        return response.Response(list(dict.fromkeys(keywords)))
