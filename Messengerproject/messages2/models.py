from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Message(models.Model):
    title  = models.CharField(max_length=100)
    slug   = models.SlugField()
    body   = models.TextField()
    date   = models.DateTimeField(auto_now_add=True)
    #thumb  = models.ImageField(default='default.png', blank=True)
    author = models.ForeignKey(User, default=None, on_delete=models.PROTECT)
    
# class Messagebank(models.Model):


    # class User (models.Model):
    # name = models.CharField(max_length=20, primary_key=True)

    def __str__(self):
        return self.title
    
    def snippet(self):
        return self.body[:50] + '...'
