from django.urls import path

from .views import hint_page, index, login_page

urlpatterns = [
    path("", login_page, name="login"),
    path("home/", index, name="index"),
    path("login/", login_page, name="login-page"),
    path("hint/<int:hint_number>/", hint_page, name="hint-page"),
]
