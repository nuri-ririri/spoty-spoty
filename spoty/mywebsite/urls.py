from django.urls import path
from . import views
from register import views as vreg

urlpatterns = [
    path("", views.home, name="home"),
    path("register/", vreg.register, name="register"),
    path("todos/", views.todos, name="todos")
]