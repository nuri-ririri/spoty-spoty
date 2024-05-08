from django.shortcuts import render, HttpResponse
from .models import ToDoItem, Album, Rating, Review


# Create your views here.
def home(request):
    albums = Album.objects.all()
    return render(request, "home.html", {"albums":albums})
def todos(request):
    items = ToDoItem.objects.all()
    return render(request, "todos.html", {"todos": items})
