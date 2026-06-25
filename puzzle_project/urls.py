from django.urls import include, path

urlpatterns = [
    path("", include("hints.urls")),
]
