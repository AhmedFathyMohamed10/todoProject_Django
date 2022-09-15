from django.contrib import admin
from .models import Task

class AdminTask(admin.ModelAdmin):
    list_display = ('title', 'completed', 'created', 'owner')

admin.site.register(Task, AdminTask)