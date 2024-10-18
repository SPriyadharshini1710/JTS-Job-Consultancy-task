from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'priority', 'status')
    list_filter = ('priority', 'status')
    search_fields = ('title', 'description')

# Alternatively, if you don't want to use the decorator:
# admin.site.register(Task, TaskAdmin)
