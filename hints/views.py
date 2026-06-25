from datetime import date

from django.conf import settings
from django.http import Http404
from django.shortcuts import render
from django.template.loader import get_template
from django.utils import timezone


def _start_date() -> date:
    try:
        return date.fromisoformat(settings.HINT_START_DATE)
    except ValueError:
        return timezone.localdate()


def _todays_hint_number() -> int | None:
    today = timezone.localdate()
    day_index = (today - _start_date()).days

    if day_index < 0:
        return None

    hint_number = day_index + 1
    if hint_number > settings.HINT_COUNT:
        return None

    return hint_number


def index(request):
    context = {
        "hint_numbers": range(1, settings.HINT_COUNT + 1),
        "start_date": _start_date(),
    }
    return render(request, "home.html", context)


def login_page(request):
    return render(request, "login.html")
