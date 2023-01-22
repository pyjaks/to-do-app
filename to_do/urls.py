from django.urls import path
from . import views
urlpatterns = [
    path("", views.ToDoListOverview.as_view(), name="index"),
]