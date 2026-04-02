from django.shortcuts import render


def index(request):
    context = {"hint_numbers": range(1, 11)}
    return render(request, "home/home.html", context)
