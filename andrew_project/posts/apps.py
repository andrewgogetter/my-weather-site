from django.apps import AppConfig


class PostsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'posts'

#this file is useful for future improvements. At the current moment we have both the "name" and "field" variables defined in our "settings.py" file