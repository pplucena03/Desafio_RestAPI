from django.db import models
from django.utils import timezone
class Event(models.Model):
    title = models.TextField(max_length=100, null=False, name='summary')
    description = models.TextField(max_length=200, blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)