from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse
from .models import ToDoList, Task

class ToDoListOverview(ListView):
    model = ToDoList
    template_name = "to_do/index.html"

class ToDoListCreateView(CreateView):
    model = ToDoList
    fields = ["title"]

class ToDoListUpdateView(UpdateView):
    model = ToDoList
    fields = ["title"]

class TaskListView(ListView):
    model = Task
    template_name = "to_do/todo_list.html"

    def get_context_data(self):
            context = super().get_context_data()
            context["todo_list"] = ToDoList.objects.get(id=self.kwargs["list_id"])
            return context

class TaskCreateView(CreateView):
    model = Task
    fields = ["todo_list", "title", "description", "due_date",]

    def get_context_data(self):
        context = super(TaskCreateView, self).get_context_data()
        todo_list = ToDoList.objects.get(id=self.kwargs["list_id"])
        context["todo_list"] = todo_list
        return context

    def get_success_url(self):
        return reverse("list", args=[self.object.todo_list_id])

class TaskUpdateView(UpdateView):
    model = Task
    fields = ["todo_list", "title", "description", "due_date",]

class TaskDeleteView(DeleteView):
    model = Task

    def get_success_url(self):
        return reverse_lazy("list", args=[self.kwargs["list_id"]])
