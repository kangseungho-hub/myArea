from django.shortcuts import render, redirect
from mylab_account.views import login_check
from .forms import DocumentForm, DirectoryForm
from .models import Document, Directory
from django.views.generic import DetailView
from myFunction.session import *

addDocumentForm = DocumentForm()

# Create your views here.

        
@login_check
def home(request):
    context = {}
    context.update({"addDocumentForm" : DocumentForm( )})
    addDirectoryForm = DirectoryForm(lab = get_session(request, "lab"))
    context.update({"addDirectoryForm" : addDirectoryForm})

    directory_list = Directory.objects.filter(lab = get_session(request, "lab"))
    context.update({"directoryList" : directory_list})
    return render(request, "mylab_home.html", context)


def Python_lab(request):
    set_session(request, "lab", "python")
    context = {}
    documents = Document.objects.all()
    context.update({"documents" : documents})

    return redirect("mylab:home")


def Java_lab(request):
    set_session(request, "lab", "java")
    context = {}
    documents = Document.objects.all()
    context.update({"documents" : documents})
    return redirect("mylab:home")


def CssHtml_lab(request):
    set_session(request, "lab", "csshtml")
    context = {}
    documents = Document.objects.all()
    context.update({"documents" : documents})
    return redirect("mylab:home")


def Go_lab(request):
    set_session(request, "lab", "go")
    context = {}
    documents = Document.objects.all()
    context.update({"documents" : documents})
    return redirect("mylab:home")


def C_lab(request):
    set_session(request, "lab", "c")
    context = {}
    documents = Document.objects.all()
    context.update({"documents" : documents})
    return redirect("mylab:home")

@login_check
def addDocument(request):
    form = DocumentForm(request.POST or None)
    if (form.is_valid()):
        form.save(request.session)
        
    print_session(request)
    return redirect("mylab:home")

def deleteDocument(request, pk):
    if request.method == "POST":
        pass

def addDirectory(request):
    if request.method == "POST":
        form = DirectoryForm(request.POST)
        if(form.is_valid()):
            form.save()
            print("it's valid!")
        print("it's unvliad!")
        print_session(request)
    return redirect("mylab:home")






def document_list(request, directory_name):
    if request.method == "GET":
        context = {}

        directory = Directory.objects.get(name = directory_name)

        documents = directory.document.all()
        context.update({"documents" : documents})

        return render(request, "mylab/document-list.html", context)


        
class detail_document(DetailView):
    template_name = "mylab/document-detail.html"
    model = Document
    form_class = DocumentForm
    context_object_name = "document"

    def get_object(self):
        return Document.objects.get(pk = self.kwargs["pk"])




    