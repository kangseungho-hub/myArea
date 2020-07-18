from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = "mylab"

urlpatterns = [
    path("", views.home, name = "home"),
    path("Python_lab", views.Python_lab, name = "Python_lab"),
    path("Java_lab", views.Java_lab, name = "Java_lab"),
    path("CssHtml_lab", views.CssHtml_lab, name = "CssHtml_lab"),
    path("Go_lab", views.Go_lab, name = "Go_lab"),
    path("C_lab", views.C_lab, name = "C_lab"),
    path("add_document", views.addDocument, name = "add_document"),
    path("add_directory", views.addDirectory, name = "add_directory"),
    path("document/<pk>", views.detail_document.as_view(), name = "detail_document"),
    path("document_list/<directory_name>", views.document_list, name = "document-list"),
]