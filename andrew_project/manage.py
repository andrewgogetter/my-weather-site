#the second line is a "shebang" line. "#!" means the following script "/usr/bin/env python" should be run in Python. In Pycharm it may be redundant
#!/usr/bin/env python
#triple quotes mean "comment"
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'andrew_project.settings') #it creates default module settings in "settings.py" right after our new project is created
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc #"from exc" helps us to locate previous exceptions, so we better know what
    execute_from_command_line(sys.argv) #"argv" means "argument vector". So we can pass multiple arguments after the first one (which is a script name). Eg "py manage.py runserver" where manage.py is [0] and runserver [1]


if __name__ == '__main__':
    main()
