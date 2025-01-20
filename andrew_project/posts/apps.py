from django.apps import AppConfig


class PostsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'posts'

#in general this code is redundant because we had already identified "BigAutoField" in the "settings.py" file