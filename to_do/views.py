from django.views.generic import ListView
from .models import ToDoList, Task

class ToDoListOverview(ListView):
    model = ToDoList
    template_name = "to_do/index.html"

class TaskListView(ListView):
    model = Task
    template_name = "to_do/todo_list.html"

    def get_context_data(self):
            context = super().get_context_data()
            context["todo_list"] = ToDoList.objects.get(id=self.kwargs["list_id"])
            return context