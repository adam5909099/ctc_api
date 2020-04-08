from django.contrib import admin
from django.db import models


class PositionManager(models.Manager):
    def move(self, obj, new_order):
        qs = self.get_queryset()

        if (obj.order > int(new_order)):
            qs.filter(order__lt=obj.order, order__gte=new_order).exclude(
                pk=obj.pk).update(order=models.F('order')+1)
        else:
            qs.filter(order__lte=new_order, order__gt=obj.order).exclude(
                pk=obj.pk).update(order=models.F('order')-1)

        obj.order = new_order
        obj.save()

    def create(self, **kwargs):
        instance = self.model(**kwargs)

        results = self.aggregate(models.Max('order'))
        current_order = results['order__max']
        if current_order is None:
            current_order = 0

        instance.order = current_order + 1
        instance.save()

        return instance


class Position(models.Model):
    name = models.CharField(max_length=255)
    order = models.IntegerField(default=1)

    objects = PositionManager()
