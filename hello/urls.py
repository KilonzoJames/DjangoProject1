from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("jack", views.jack, name="jack"),
    path("<str:name>", views.greet, name="greet"),
    path("html", views.indexhtml, name = "indexhtml")
]
