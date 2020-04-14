from rest_framework import serializers
from .models import Job
from pdfminer.high_level import extract_text
import string


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
        instance.resume = validated_data.get('resume')
        printable = set(string.printable)
        resume_text = extract_text(validated_data.get('resume'))
        instance.resume_text = ''.join(
            filter(lambda x: x in printable, resume_text)).strip().strip('\n')
        instance.save()
        return instance
