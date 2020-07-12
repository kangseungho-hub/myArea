from django.urls import path
from . import views


app_name = "mylab"
urlpatterns = [
    path("", views.mylab_account, name = "account"),
    path("Python_lab", views.Python_lab, name = "Python_lab"),
    path("Java_lab", views.Java_lab, name = "Java_lab"),
    path("CssHtml_lab", views.CssHtml_lab, name = "CssHtml_lab"),
    path("Go_lab", views.Go_lab, name = "Go_lab"),
    path("C_lab", views.C_lab, name = "C_lab"),
    path("login", views.Login, name = "login"),
    path("accountExistCheck", views.accountExistCheck, name = "accountExistCheck"),
    path("signup", views.SignUp, name = "signup"),
    path("emailExistCheck", views.emailExistCheck, name = "emailExistCheck"),
    path("usernameExistCheck", views.usernameExistCheck, name = "usernameExistCheck"),
    path("logout", views.Logout, name = "logout"),
]