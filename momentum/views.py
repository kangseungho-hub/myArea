from django.shortcuts import render

# Create your views here.


def momentum(request):
    return render(request, "momentum.html")


def test(request):
    return render(request, "test.html")