from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

#in general this code is redundant because we had already identified "BigAutoField" in the "settings.py" file