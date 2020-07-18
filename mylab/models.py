from django.db import models
from django.shortcuts import reverse
from ckeditor_uploader.fields import RichTextUploadingField



class Directory(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length = 30, default = "None")
    lab = models.CharField(max_length = 20)

    def __str__(self):
        return self.name 

class Document(models.Model):
    objects = models.Manager()
    directory = models.ForeignKey(Directory, on_delete=models.CASCADE, related_name="document")
    
    title = models.CharField(max_length = 100)
    developer = models.CharField(max_length = 20)
    
    content = RichTextUploadingField(blank = True, null = True)
    date = models.DateTimeField(auto_now_add= True)
    check_count = models.IntegerField(default = 0)

    def get_absolute_url(self):
        return reverse("mylab:detail_document", args = [self.pk])




    






# Create your models here.
