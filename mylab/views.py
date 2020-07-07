from django.shortcuts import render
from django.http import HttpResponse


def mylab_home(request):
    return render(request, "mylab_home.html")
