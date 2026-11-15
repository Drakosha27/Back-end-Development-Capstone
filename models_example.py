# Move into the models.py of your Django app, after running startproject/startapp.
from django.db import models
from django.utils import timezone
class Concert(models.Model):
    concert_name = models.CharField(max_length=255)
    event_date = models.DateField(default=timezone.localdate)
    def __str__(self): return self.concert_name
