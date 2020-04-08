from rest_framework import viewsets, status, parsers, response, decorators
from .models import Position
from .serializers import PositionSerializer


class PositionViewSet(viewsets.ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer

    @decorators.action(detail=True, methods=['PUT'])
    def move(self, request, pk):
        obj = self.get_object()
        new_order = request.data.get('order')
        Position.objects.move(obj, new_order)
        return response.Response()
