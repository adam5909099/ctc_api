from django.db import models


class Position(models.Model):
    name = models.CharField(max_length=255)


class Resume(models.Model):
    name = models.CharField(max_length=255)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
