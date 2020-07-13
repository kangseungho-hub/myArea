from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, "mylab_home.html")
    
def Python_lab(request):
    context = {"where" : "Python"}
    return render(request, "lab.html", context)

def Java_lab(request):
    context = {"where" : "java"}
    return render(request, "lab.html", context)

def CssHtml_lab(request):
    context = {"where" : "csshtml"}
    return render(request, "lab.html", context)

def Go_lab(request):
    context = {"where" : "go"}
    return render(request, "lab.html", context)

def C_lab(request):
    context = {"where" : "c"}
    return render(request, "lab.html" , context)