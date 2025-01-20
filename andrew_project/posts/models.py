from django.db import models
from django.contrib.auth.models import User #the "User" model getting created when we register a new user and it stored in our database

# Create your models here.

class Post(models.Model): #this model will be stored in our database
    title=models.CharField(max_length=100)
    body=models.TextField()
    slug=models.SlugField()
    date=models.DateTimeField(auto_now_add=True)
    banner=models.ImageField(default="fallback.png",blank=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE,default=None) #it means that if a user get deleted all their posts will be deleted too

    def __str__(self): #it helps us to see the posts names on the admin site
        return self.title