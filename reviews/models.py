from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg
# Create your models here.


class Review(models.Model):
    header = models.Charfield(Max_length=150, default="Header")
    text = models.TextField()

    def average_rating(self) -> float:
        return Rating.object.filter(post=self).aggregate(Avg("rating"))["rating__avg"] or 0
   
    def __str__(self):
        return f"{self.header}: {self.avergae_rating()}"


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.post.header}: {self.rating}"
