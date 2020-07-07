from django.urls import path
from . import views


app_name = "mylab"
urlpatterns = [
    path("", views.mylab_home, name = "home"),
]