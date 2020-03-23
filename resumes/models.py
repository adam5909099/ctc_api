from django.db import models


class Resume(models.Model):
    name = models.CharField(max_length=255)
