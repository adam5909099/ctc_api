from rest_framework import serializers
from .models import Job
from pdfminer.high_level import extract_text
import string
import re


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

        extracted = extract_text(validated_data.get('resume'))
        printable = ''.join(
            filter(lambda x: x in set(string.printable), extracted))
        without_cid = re.sub(r'\(cid:\d*\)', '', printable)
        stripped = re.sub('\n{2,}', '\n\n', without_cid).strip().strip('\n')
        instance.resume_text = stripped

        instance.save()
        return instance
