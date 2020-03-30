from rest_framework import serializers
from .models import Job, Position


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'
        read_only_fields = ['resume']


class JobResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ['resume']


class PositionSerializer(serializers.ModelSerializer):
    jobs = JobSerializer(many=True, read_only=True)

    class Meta:
        model = Position
        fields = '__all__'
