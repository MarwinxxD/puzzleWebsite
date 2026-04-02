from django.http import Http404
from django.shortcuts import render
from django.template.loader import get_template


def index(request):
    context = {"hint_numbers": range(1, 8)}
    return render(request, "home/home.html", context)


def hint_page(request, hint_number):
    if hint_number not in range(1, 8):
        raise Http404("Hint not found")

    template_name = f"hints/hint{hint_number}.html"
    try:
        get_template(template_name)
    except Exception as exc:
        raise Http404("Hint template missing") from exc

    return render(request, template_name, {"hint_number": hint_number})
