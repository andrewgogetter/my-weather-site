"""
ASGI config for andrew_project project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'andrew_project.settings')

application = get_asgi_application()


#asgi is better for concurrency like chat applications, and can handle both types whereas wsgi is better for apps that handle request one by one