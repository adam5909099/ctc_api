from rest_framework import serializers
from .models import Job
from pdfminer.high_level import extract_text
import string
import re
import json
from utils.emsi import get_keywords


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'
        read_only_fields = ['resume']

    keywords = serializers.SerializerMethodField()

    def get_keywords(self, obj):
        if obj:
            return json.loads(obj.keywords)
        else:
            return null

    def create(self, validated_data):
        instance = Job.objects.create(**validated_data)
        instance.keywords = json.dumps(get_keywords(validated_data.get('description')))
        instance.save()
        return instance


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
