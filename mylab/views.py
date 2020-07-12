from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .forms import LoginForm, SignUpForm, FindAccountForm
from django.views.generic import View
from django.core.mail import send_mail
from .models import User
import json

def mylab_account(request):
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
    if request.method == "POST":
        loginForm = LoginForm(request.POST)
        if(loginForm.is_valid()):
            request.session["username"] = loginForm.cleaned_data["UserName"]
            request.session["PW"] = loginForm.cleaned_data["PW"]
            return render(request, "mylab_home.html")
        return redirect("mylab:account")




def SignUp(request):
    if request.method == "GET":
        email = request.GET["email"]
    if request.method == "POST":
        signupForm = SignUpForm(request.POST)

        if signupForm.is_valid():
            signupForm.save(request.META["REMOTE_ADDR"])
            return redirect("mylab:account")

        return redirect("mylab:account")
    return redirect("mylab:account")


def accountExistCheck(request):
    resp = {"accountExist" : None}
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        if(User.objects.filter(UserName = username, PW = password).exists()):
            resp["accountExist"] = True
        else:
            resp["accountExist"] = False
        return HttpResponse(json.dumps(resp), content_type = "application/json")

def emailExistCheck(request):
    print(request.POST)
    resp = {"emailExist" : None}
    if request.method == "GET":    
        if(User.objects.filter(Email = request.GET["email"]).exists()):
            resp["emailExist"] = True
        else:
            resp["emailExist"] = False
        return HttpResponse(json.dumps(resp), content_type = "application/json")

def usernameExistCheck(request):
    resp = {"usernameExist" : None}
    if request.method == "GET":
        if(User.objects.filter(UserName = request.GET["username"]).exists()):
            resp["usernameExist"] = True
        else:
            resp["usernameExist"] = False
        return HttpResponse(json.dumps(resp), content_type = "application/json")

        
def Logout(request):
    pass
    
    


    




