from django.urls import path
from . import views


app_name = "mylab_account"

urlpatterns = [
    path("", views.mylab_account, name = "account"),
    path("login", views.Login, name = "login"),
    path("accountExistCheck", views.accountExistCheck, name = "accountExistCheck"),
    path("signup", views.SignUp, name = "signup"),
    path("emailExistCheck", views.emailExistCheck, name = "emailExistCheck"),
    path("usernameExistCheck", views.usernameExistCheck, name = "usernameExistCheck"),
    path("findAccount", views.findAccount, name = "findAccount"),
    path("logout", views.Logout, name = "logout"),
]