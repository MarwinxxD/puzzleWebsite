from django.urls import path

from .views import hint_page, index

urlpatterns = [
    path("", index, name="index"),
    path("hint/<int:hint_number>/", hint_page, name="hint-page"),
]
