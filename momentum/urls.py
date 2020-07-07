from django.urls import path
from . import views

app_name = "momentum"
urlpatterns = [
    path("", views.momentum),
    path("test", views.test),
]