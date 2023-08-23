#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import subprocess


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proxy.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    # sys.path.append(sys.path[0][:-6])
    # sys.path.append(sys.path[0][:-6] + "/configuration/paths.py")
    # exec(open(sys.path[len(sys.path) - 1]).read())
    for i in range(len(sys.path)):
        if sys.path[i][-7:] == 'my_shop':
            sys.path.append(sys.path[i])
            sys.path.append(sys.path[i] + "/configuration/paths.py")
            break
        elif sys.path[i][-5:] == 'proxy':
            sys.path.append(sys.path[i][:-6])
            sys.path.append(sys.path[i][:-6] + "/configuration/paths.py")
            break
    exec(open(sys.path[len(sys.path) - 1]).read())
    main()
