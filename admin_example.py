# Place inside your Django application's admin.py
from django.contrib import admin
from .models import Concert
admin.site.register(Concert)
