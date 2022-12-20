from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Review(models.Model):

    review_tag_choices = [
        ('game', 'Game'),
        ('Film', 'film'),
        ('Boardgame', 'boardgame'),
        ('Book', 'book'),
        ('Tv Series', 'tv series'),
        ('Blank', 'blank')
    ]   

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    header = models.CharField(max_length=150, default="Header")
    text = models.TextField(blank=True)
    rating = models.IntegerField(default="0")
    created_on = models.DateTimeField(auto_now_add=True)
    review_tag = models.CharField(
        max_length=32, choices=review_tag_choices, default='blank'
    )

    def __str__(self):
        return f"{self.header}: {self.rating} out of 10"
