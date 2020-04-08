from rest_framework import serializers
from .models import Job


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'
        read_only_fields = ['resume']


class ResumeUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ['resume']
