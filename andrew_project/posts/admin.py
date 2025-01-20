from django.contrib import admin
from .models import Post

# Register your models here.

admin.site.register(Post)

#when we create a new model in our "models.py" file then we have to register it here to be able to see it on our admin site and modify it. If we forget, our project will still be working, but we can't modify our model on the admin site