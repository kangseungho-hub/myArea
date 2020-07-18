from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .forms import LoginForm, SignUpForm, FindAccountForm
from django.views.generic import View
from .models import User
import json



def login_check(active):
    def wrapper(*a, **k):
        user_has_login = a[0].session.get("username", "nob")
        if ( user_has_login == "nob"):
            return redirect("mylab_account:account")
        else:
            return active(*a, *k)
    return wrapper


def mylab_account(request):
        login_form = LoginForm()
        signup_form = SignUpForm()
        find_account_form = FindAccountForm()

        Form = { "LoginForm" : login_form, "SignupForm" : signup_form, "FindAccountForm" : find_account_form}
        resp = render(request, "mylab_account.html", Form)
        return resp
            

    
            




def Login(request):
    if request.method == "POST":
        loginForm = LoginForm(request.POST)
        if(loginForm.is_valid()):
            request.session["username"] = loginForm.cleaned_data["UserName"]
            request.session["PW"] = loginForm.cleaned_data["PW"]
            return redirect("mylab:home")
        return redirect("mylab_account:account")




def SignUp(request):
    if request.method == "GET":
        email = request.GET["email"]
    if request.method == "POST":
        signupForm = SignUpForm(request.POST)

        if signupForm.is_valid():
            signupForm.save(request.META["REMOTE_ADDR"])
            return redirect("mylab_account:account")

        return redirect("mylab_account:account")
    return redirect("mylab_account:account")


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


def findAccount(request):
    return redirect("mylab_account:account")


def Logout(request):
    try:
        del request.session["username"]
    except KeyError:
        pass

    return redirect("mylab_account:account")
    

    
    


    




