from django.views.generic import ListView
from .models import ToDoList

class ToDoListOverview(ListView):
    model = ToDoList
    template_name = "to_do/index.html"