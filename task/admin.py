from django.contrib import admin
from .models import Task_template, Type, Field_name

class Task_templateAdmin(admin.ModelAdmin):
    list_display = ['id','name']

class TypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

class Field_nameAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'type', 'task_template']

admin.site.register(Type, TypeAdmin)
admin.site.register(Task_template, Task_templateAdmin)
admin.site.register(Field_name, Field_nameAdmin)