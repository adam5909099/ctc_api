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

    def create(self, instance, validated_data):
        instance.title = validated_data.get('title')
        instance.company = validated_data.get('company')
        instance.location = validated_data.get('location')
        instance.logo = validated_data.get('logo')
        instance.description = validated_data.get('description')
        instance.position = validated_data.get('position')
        instance.url = validated_data.get('url')
        instance.keywords = validated_data.get('resume')



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
