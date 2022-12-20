from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Review(models.Model):

    review_tag_choices = [
        ('game', 'Game'),
        ('film', 'Film'),
        ('boardgame', 'Boardgame'),
        ('book', 'Book'),
        ('tv series', 'Tv Series'),
        ('blank', 'Blank')
    ]

    rating_choice = [
        ('_0', '0'), 
        ('_1', '1'), 
        ('_2', '2'), 
        ('_3', '3'), 
        ('_4', '4'), 
        ('_5', '5'), 
        ('_6', '6'), 
        ('_7', '7'), 
        ('_8', '8'), 
        ('_9', '9'), 
        ('_10', '10'), 
    ]

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    header = models.CharField(max_length=150, default="Header")
    text = models.TextField(blank=True)
    rating = review_tag = models.CharField(
        max_length=5, choices=rating_choice, default='0'
    )
    created_on = models.DateTimeField(auto_now_add=True)
    review_tag = models.CharField(
        max_length=32, choices=review_tag_choices, default='blank'
    )

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"{self.header}: {self.rating} out of 10"
