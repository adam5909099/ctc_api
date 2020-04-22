from django.contrib import admin
from django.db import models
from positions.models import Position


class Job(models.Model):
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    logo = models.CharField(max_length=255, blank=True)
    description = models.TextField()
    keywords = models.TextField(blank=True)
    position = models.ForeignKey(
        Position, on_delete=models.CASCADE, related_name='jobs')
    url = models.URLField(default="")
    resume = models.FileField(upload_to="", blank=True)
    resume_text = models.TextField(default="")
    resume_keywords = models.TextField(blank=True)
    score = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
