from django.contrib import admin
from .models import Post

# Register your models here.

admin.site.register(Post)

#if we create models then we have to register them on the admin site