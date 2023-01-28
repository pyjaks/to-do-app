from django.views.generic import ListView
from .models import ToDoList, Task

class ToDoListOverview(ListView):
    model = ToDoList
    template_name = "to_do/index.html"

class TaskListView(ListView):
    model = Task
    template_name = "to_do/todo_list.html"

