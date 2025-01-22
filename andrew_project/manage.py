#!/usr/bin/env python #the "#!" symbols mean shebang which is telling to run this code in Python. It's no need to use it in PyCharm
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'andrew_project.settings') #it sets our django module to the "settings.py" file. This line of code instructs our Django project to use settings from the "settings.py" file
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc #"from exc" means that we can trace the previous exceptions, not only the last one
    execute_from_command_line(sys.argv) #argv means argument vector which allows us to pass args after the very first one. Eg "py manage.py runserver" where the first arg is a script name "manage.py" and the second one "runserver". Without "argv" we would be able to pass only the script name


if __name__ == '__main__':
    main()

#this file allows us to run admin tasks in our terminal