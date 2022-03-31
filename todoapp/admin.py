from django.contrib import admin
from .models import TodoModel

class TodoAdmin(admin.ModelAdmin):
    pass

admin.site.register(TodoModel, TodoAdmin)