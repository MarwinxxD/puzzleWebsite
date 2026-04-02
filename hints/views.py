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
    return render(request, "home/home.html", context)


def hint_page(request, hint_number):
    if hint_number not in range(1, settings.HINT_COUNT + 1):
        raise Http404("Hint not found")

    template_name = f"hints/hint{hint_number}.html"
    try:
        get_template(template_name)
    except Exception as exc:
        raise Http404("Hint template missing") from exc

    start = _start_date()
    hint_unlock_date = start + __import__("datetime").timedelta(days=hint_number - 1)
    today = timezone.localdate()
    days_until_unlock = (hint_unlock_date - today).days
    is_available = days_until_unlock <= 0

    context = {
        "hint_number": hint_number,
        "is_available": is_available,
        "unlock_date": hint_unlock_date,
        "days_until_unlock": max(0, days_until_unlock),
    }
    return render(request, template_name, context)
