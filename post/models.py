from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):

    post_tag_choices = [
        ('game', 'Game'),
        ('film', 'Film'),
        ('boardgame', 'Boardgame'),
        ('book', 'Book'),
        ('tv series', 'Tv Series'),
    ]

    title = models.CharField(max_length=200, unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField(blank=True)
    featured_image = models.ImageField(
        upload_to='images/', default='../jqfjapljyx3yvl5nspm1', blank=True
    )
    created_on = models.DateTimeField(auto_now_add=True)
    post_tag = models.CharField(
        max_length=32, choices=post_tag_choices, default='game'
    )

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f'{self.id} {self.title}'
