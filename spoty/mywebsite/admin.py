from django.contrib import admin
from .models import ToDoItem, Album, Review, Rating
# Register your models here.

admin.site.register(ToDoItem)
admin.site.register(Album)
admin.site.register(Review)
admin.site.register(Rating)