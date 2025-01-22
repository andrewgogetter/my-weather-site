from django.db import models
from django.contrib.auth.models import User
#This "User" that we import from contrib will be created when we accomplish the register procedure on our website

# Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=100)
    body=models.TextField()
    slug=models.SlugField() #slug is the special type of chars that contain eg hyphens, slashes, etc. It's used for the url structure
    date=models.DateTimeField(auto_now_add=True)
    banner=models.ImageField(default="fallback.png",blank=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE,default=None) #it means if a user gets deleted then all their posts get deleted

    def __str__(self): #with this we can post names on the admin site
        return self.title