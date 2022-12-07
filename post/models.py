from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):

    featured_image_filter_choices = [
        ('_1977', '1977'), 
        ('brannan', 'Brannan'),
        ('earlybird', 'Earlybird'), 
        ('hudson', 'Hudson'),
        ('inkwell', 'Inkwell'), 
        ('lofi', 'Lo-Fi'),
        ('kelvin', 'Kelvin'), 
        ('normal', 'Normal'),
        ('nashville', 'Nashville'), 
        ('rise', 'Rise'),
        ('toaster', 'Toaster'), 
        ('valencia', 'Valencia'),
        ('walden', 'Walden'), 
        ('xpro2', 'X-pro II')
    ]   

    title = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField(blank=True)
    featured_image = models.ImageField(
        upload_to='images/', default='../jqfjapljyx3yvl5nspm1', blank=True
    )
    featured_image_filter = models.CharField(
        max_length=32, choices=featured_image_filter_choices, default='normal'
    )
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f'{self.id} {self.title}'