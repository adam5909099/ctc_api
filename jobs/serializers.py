from rest_framework import serializers
from .models import Job
from pdfminer.high_level import extract_text
import string
import re
import json
from utils.emsi import get_keywords


class JobSerializer(serializers.ModelSerializer):
    keywords = serializers.SerializerMethodField()
    resume_keywords = serializers.SerializerMethodField()

    def get_keywords(self, obj):
        return json.loads(obj.keywords) if obj.keywords else None

    def get_resume_keywords(self, obj):
        return json.loads(obj.resume_keywords) if obj.resume_keywords else None

    def create(self, validated_data):
        instance = Job.objects.create(**validated_data)
        instance.keywords = json.dumps(
            get_keywords(validated_data.get('description')))
        instance.save()
        return instance

    class Meta:
        model = Job
        fields = '__all__'
        read_only_fields = ['resume']


class ResumeUploadSerializer(serializers.ModelSerializer):
    def update(self, instance, validated_data):
        instance.resume = validated_data.get('resume')

        extracted = extract_text(validated_data.get('resume'))
        printable = ''.join(
            filter(lambda x: x in set(string.printable), extracted))
        without_cid = re.sub(r'\(cid:\d*\)', '', printable)
        stripped = re.sub('\n{2,}', '\n\n', without_cid).strip().strip('\n')
        instance.resume_text = stripped

        resume_keywords = get_keywords(stripped)
        instance.resume_keywords = json.dumps(resume_keywords)

        skills = list(map(lambda x: x['skill'], json.loads(instance.keywords)))
        resume_skills = list(map(lambda x: x['skill'], resume_keywords))
        matching_count = len([skill for skill in skills if skill in resume_skills])
        instance.score = matching_count / len(skills) if len(skills) else 0

        instance.save()
        return instance

    class Meta:
        model = Job
        fields = ['resume', 'resume_text', 'resume_keywords', 'score']
