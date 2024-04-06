from django.db import models

class Event(models.Model):
    event_name = models.CharField(max_length=100)
    city_name = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    latitude = models.FloatField()
    longitude = models.FloatField()
