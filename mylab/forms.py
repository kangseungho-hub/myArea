from django import forms
from .models import Document, Directory

class DirectoryForm(forms.ModelForm):
    class Meta:
        model = Directory
        fields = [
            "name",
            "lab",
        ]
    
    def __init__(self, *args, **kwargs):
        lab = kwargs.pop("lab", None)
        super(DirectoryForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].label = False
        self.fields["name"].widget.attrs.update({"class" : "add-directory-name"})
        self.fields["lab"].widget.attrs.update({"class" : "add-directory-name", "readonly" : "true", "value" :lab })
        
        
    def clean_name(self):
        name = self.cleaned_data["name"]
        if len(name) < 1 or len(name) > 50:
            raise forms.ValidationError("directory name must longer than 1character and shorter than 50 character")
        return name

    def save(self, *args, **kwargs):
        newDirectory = Directory(name = self.cleaned_data["name"], lab = self.cleaned_data["lab"])
        newDirectory.save()
        print("saved!")


    


class DocumentForm(forms.ModelForm):
    directory_name = forms.CharField()
    class Meta:
        model = Document
        #had to add developer when save form
        #had to add lab when save form

        #date is auto add
        fields = [
            "title", 
            "content",
            "directory_name",
        ]

    def __init__(self, *args, **kwargs):
        super(DocumentForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].label = False
        self.fields["title"].widget.attrs.update({"class" : "document-title-input"})
        self.fields["content"].widget.attrs.update({"class" : "document-content-input"})
        self.fields["directory_name"].widget.attrs.update({"class" : "document-directory-input", "readonly" : "true" })

    def save(self, session):
        data = self.cleaned_data
        newDocument = Document(
            developer =session["username"],
            title = data["title"],
            content = data["content"],
            directory = Directory.objects.get(name = data["directory_name"])
        )
        newDocument.save()

        


        



    