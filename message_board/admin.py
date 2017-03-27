from django.contrib import admin

# Register your models here.
from .models import Topic,Message

admin.site.register(Topic)
admin.site.register(Message)
