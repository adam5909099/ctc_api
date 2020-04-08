from rest_framework import serializers
from .models import Position
from jobs.serializers import JobSerializer


class PositionSerializer(serializers.ModelSerializer):
    jobs = JobSerializer(many=True, read_only=True)

    class Meta:
        model = Position
        fields = '__all__'
