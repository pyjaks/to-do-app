from django.urls import path
from . import views
urlpatterns = [
    path("", views.ToDoListOverview.as_view(), name="index"),
    path("list/<int:list_id>/",
        views.TaskListView.as_view(), name="list"),
]