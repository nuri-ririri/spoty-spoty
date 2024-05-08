from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ToDoItem(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

class Album(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=100)
    release_date = models.DateField()
    genre = models.CharField(max_length=50)
    #При дальнейшей разработке, добавлю датабазу изображений

    
    def __str__(self):
        return f"{self.title} created by {self.artist}"
    
class Review(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    review_text = models.TextField
    review_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reviewed by {self.user.username} on {self.album.title}"

class Rating(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name="ratings")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="ratings")
    rating = models.TextField
    rating_date = models.DateTimeField()

    def __str__(self):
        return f'{self.rating}/10 by {self.user.username} for the album/single "{self.album.title}"'
    