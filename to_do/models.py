from datetime import datetime, timedelta

from django.db import models
from django.urls import reverse


class ToDoList(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.title

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(default=(datetime.now() + timedelta(weeks=1)))
    todo_list = models.ForeignKey(ToDoList, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} due on {self.due_date}"

    def get_absolute_url(self):
        return reverse(
            "edit-task", args=[str(self.todo_list.id), str(self.id)]
    )
