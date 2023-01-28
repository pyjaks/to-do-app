from django.contrib import admin
from to_do.models import ToDoList, Task

# Register your models here.

admin.site.register(ToDoList)
admin.site.register(Task)
