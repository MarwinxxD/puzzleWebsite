import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "puzzle_project.settings")

application = get_wsgi_application()

# Alias kept for platforms that look for `app` in WSGI modules.
app = application
