from rest_framework import serializers
from .models import Job
from pdfminer.high_level import extract_text


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'
        read_only_fields = ['resume']


class ResumeUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ['resume', 'resume_text']

    def update(self, instance, validated_data):
        instance.resume_text = extract_text(validated_data.get('resume'))
        return instance
