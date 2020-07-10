from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .forms import LoginForm, SignUpForm, FindAccountForm


def mylab_home(request):
    login_form = LoginForm()
    signup_form = SignUpForm()
    find_account_form = FindAccountForm()
    Form = { "LoginForm" : login_form, "SignupForm" : signup_form, "FindAccountForm" : find_account_form}
    return render(request, "mylab_account.html", Form)


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
    return render(request, "lab/c_lab.html" , context)


def Login(request):
    pass

def SignUp(request):
    pass

def Logout(request):
    pass
    
    


    




