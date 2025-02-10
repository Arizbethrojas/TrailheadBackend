from django.contrib import admin
from .models import TodoItem, Notification

# Register your models here. so they appear in our admin panel, allowing us to modify and view them 
admin.site.register(TodoItem)
admin.site.register(Notification)