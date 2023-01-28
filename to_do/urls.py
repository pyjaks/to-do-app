from django.urls import path
from . import views
urlpatterns = [
    path("", views.ToDoListOverview.as_view(), name="index"),
    path("list/<int:list_id>/",
        views.TaskListView.as_view(), name="list"),
    path("list/<int:list_id>/task/new/",
        views.TaskCreateView.as_view(), name="new-task"),
    path("list/<int:list_id>/task/<int:pk>/", 
        views.TaskUpdateView.as_view(), name="edit-task"),
    path("list/<int:list_id>/task/<int:pk>/delete/",
        views.TaskDeleteView.as_view(), name="delete-task"),
]